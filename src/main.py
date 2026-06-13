from config.ingest import Ingestion

def main():
    source_to_ingest_from = Ingestion("../test-files/yellow_trip_2026.parquet", 10).ingest_parquet()
    print(source_to_ingest_from.head(10).collect())
    print("hello?")
    return


if __name__ == "__main__":
    main()