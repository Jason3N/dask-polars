import polars as pl

class Ingestion:
    def __init__(self, path: str, n_rows=int):
        self.path = path
        self.n_rows = n_rows


    def ingest_parquet(self) -> pl.LazyFrame:
        # ingest
        return pl.scan_parquet(source=self.path, n_rows=self.n_rows)
