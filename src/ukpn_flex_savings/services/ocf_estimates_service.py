
from ukpn_flex_savings.connectors.ocf_solar_estimates_connectors import OCFSolarEstimatesConnector
from ukpn_flex_savings.repositories.ocf_solar_estimate_repository import OCFEstimateRepository



class OCFEstimatesService:
    
    def __init__(self, ocf_estimates_connector: OCFSolarEstimatesConnector,
                 ocf_estimates_repository: OCFEstimateRepository):
        self.ocf_estimates_connector = ocf_estimates_connector
        self.ocf_estimates_repository = ocf_estimates_repository
    
    def get_and_save_ocf_estimates(self, filename: str):
        print(f"Fetching OCF estimates from connector for file: {filename}...")
        df =  self.ocf_estimates_connector.fetch_ocf_estimates(filename)
        if df is not None:
            print(f"OCF estimates loaded from connector: {filename}")
            return df
        
        filename = f"{filename}.parquet"
        
        self.ocf_estimates_repository.save_ocf_estimates(df, filename)
    
        
        
        