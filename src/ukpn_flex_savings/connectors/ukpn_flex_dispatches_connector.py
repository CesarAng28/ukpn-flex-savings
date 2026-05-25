from datetime import datetime, time 
import httpx
import polars as pl
import pandas as pd


from ukpn_flex_savings.models import FlexDispatches

class UKPNFlexDispatchesConnector:
    def __init__(self, dispatch_url:str, api_key:str):
        self.api_key = api_key
        self.dispatch_url = dispatch_url
        
    def fetch_dispatches(self, 
                         start_time:datetime, 
                         end_time:datetime,
                         ) -> pl.DataFrame:
        params = {
            "start_time_local>": start_time.isoformat(),
            "end_time_local<": end_time.isoformat(),
            "apikey": self.api_key
            
        }
        response = httpx.get(self.dispatch_url, params=params)
        response.raise_for_status()
        data = response.json()
        print(data)
        df = pl.DataFrame(data["results"])
        print(df.head())
        df = df.with_columns(pl.col("start_time_local").str.to_datetime(time_zone="UTC").alias("start_time_local"),
                       pl.col("end_time_local").str.to_datetime(time_zone="UTC").alias("end_time_local"),
                       pl.col("time_utc").str.slice(0, 8).str.strptime(pl.Time, format="%H:%M:%S").alias("time_utc"))
        df = self.validate_dispatches(df)
        return df
        
    def validate_dispatches(self, dispatches: pl.DataFrame) -> pl.DataFrame:
        
        validated_dispatches = [
            FlexDispatches.model_validate(dispatch) for dispatch in dispatches.iter_rows(named=True)
        ]
        dispatches = pl.DataFrame([dispatch.model_dump() for dispatch in validated_dispatches])
        
        return dispatches
        
        
