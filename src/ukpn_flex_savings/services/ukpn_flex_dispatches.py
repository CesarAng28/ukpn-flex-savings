from datetime import datetime


import polars as pl


from ukpn_flex_savings.connectors import UKPNFlexDispatchesConnector
from ukpn_flex_savings.repositories import UKPNFlexDispatchesRepository

class UKPNFlexDispatchesService:
    def __init__(self, 
                 ukpn_connector: UKPNFlexDispatchesConnector,
                 repository: UKPNFlexDispatchesRepository) -> None:
        
        self.ukpn_connector = ukpn_connector
        self.ukpn_repository = repository
    
    def fetch_and_save_dispatches(self, start_time: datetime, end_time: datetime) -> pl.DataFrame:
        
        
        print(f"Fetching dispatches from {start_time} to {end_time}...")
        dispatches = self.ukpn_connector.fetch_dispatches(start_time, end_time)
        print(f"Fetched {len(dispatches)} dispatches. Saving to repository...")
        filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_flex_dispatches.parquet"
        file_path = self.ukpn_repository.save_dispatches(dispatches, filename)
        print(f"Flex dispatches saved to: {file_path}")
        return file_path
    
        
        