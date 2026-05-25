from pathlib import Path

import polars as pl


class UKPNFlexDispatchesRepository:

    def __init__(self, base_dir: str = "data/bronze/ukpn"):
        self.base_dir = Path(base_dir)

    def save_dispatches(
        self,
        df: pl.DataFrame,
        filename: str,
    ) -> Path:

        self.base_dir.mkdir(parents=True, exist_ok=True)

        path = self.base_dir / filename

        df.write_parquet(path)

        return path

    def load_dispatches(
        self,
        filename: str,
    ) -> pl.DataFrame:

        path = self.base_dir / filename

        return pl.read_parquet(path)