from pathlib import Path

import polars as pl

class UKPNFlexDispatchesRepository:
    def __init__(self, data_dir:Path):
        self.data_dir = Path(data_dir)
        
    def save_dispatches(self, 
                        dispatches: pl.DataFrame, 
                        filename:str) -> Path:
        
        self.data_dir.mkdir(parents=True, exist_ok=True)
        file_path = self.data_dir / filename
        dispatches.write_parquet(file_path)
        return file_path
        
        
        
        
    def load_dispatches(self, 
                        filename:str) -> pl.DataFrame:
        
        file_path = self.data_dir / filename
        return pl.read_parquet(file_path)