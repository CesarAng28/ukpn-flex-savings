from datetime import datetime


import polars as pl

from ukpn_flex_savings.config import settings
from ukpn_flex_savings.connectors import UKPNFlexDispatchesConnector
from ukpn_flex_savings.repositories import UKPNFlexDispatchesRepository

class UKPNFlexDispatchesService:
    def __init__(self, 
                 connectors: UKPNFlexDispatchesConnector,
                 repository: UKPNFlexDispatchesRepository):
        self.connectors = connectors
        self.repository = repository
        
    
        dispatches = self.connectors.fetch_dispatches(settings.start_time, settings.end_time)
        
        filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_flex_dispatches.parquet"
        file_path = self.repository.save_dispatches(dispatches, filename)
        return file_path
    
        
        