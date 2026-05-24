from datetime import datetime
import httpx
import polars as pl

from ukpn_flex_savings.config import settings

class UKPNFlexDispatchesService:
    def __init__(self, dispatch_url:str, api_key:str):
        self.api_key = api_key
        self.dispatch_url = dispatch_url
        
    def fetch_dispatches(self, 
                         start_time:datetime, 
                         end_time:datetime,
                         ) -> pl.DataFrame:
        params = {
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "api_key": self.api_key,
        }
        response = httpx.get(self.dispatch_url, params=params)
        response.raise_for_status()
        data = response.json()
        records = data.get("records", [])
        dispatches = [record["fields"] for record in records]
        df = pl.DataFrame(dispatches)
        return df.with_columns(pl.col("start_time").str.to_datetime().alias("start_time"),
                               pl.col("end_time").str.to_datetime().alias("end_time"))