
from pathlib import Path

import polars as pl


class OCFEstimateRepository:
    
    def __init__(self, data_dir: str):
        self.data_dir = data_dir
        
    def save_ocf_estimates(self, df: pl.DataFrame, filename: str) -> Path:
        self.data_dir.mkdir(parents=True, exist_ok=True)
        file_path = Path(self.data_dir) / filename
        df.write_parquet(file_path)
        return file_path
    
    def load_ocf_estimates(self, filename: str) -> pl.DataFrame:
        file_path = Path(self.data_dir) / filename
        
        df = pl.read_parquet(file_path)
        
        df = df.with_columns(pl.col("timestamp_utc").str.to_datetime(time_zone="UTC").alias("timestamp_utc"))
        df = self.validate_ocf_estimates(df)
        
        return df
    
