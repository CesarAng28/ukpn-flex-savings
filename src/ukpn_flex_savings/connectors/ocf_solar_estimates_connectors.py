from datetime import datetime

import polars as pl

from ukpn_flex_savings.models.ocf_models import OCFEstimates

class OCFSolarEstimatesConnector:
    
    def __init__(self, data_dir: str):
        self.data_dir = data_dir
    
    def fetch_ocf_estimates(self, filename: str) -> pl.DataFrame:
        file_path = f"{self.data_dir}/{filename}"
        
        df = pl.read_csv(file_path)
        
        df = df.with_columns(pl.col("timestamp_utc").str.to_datetime(time_zone="UTC").alias("timestamp_utc"))
        df = self.validate_ocf_estimates(df)
        
        return df
    
    def validate_ocf_estimates(self, ocf_estimates: pl.DataFrame) -> pl.DataFrame:
        validated_estimates = [
            OCFEstimates.model_validate(estimate) for estimate in ocf_estimates.iter_rows(named=True)
        ]
        ocf_estimates = pl.DataFrame([estimate.model_dump() for estimate in validated_estimates])
        
        return ocf_estimates