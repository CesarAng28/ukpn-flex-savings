
from datetime import datetime

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    
    data_dir: str

    ukpn_dispatches_url: str
    ukpn_api_key: str
    default_flex_price_gbp_per_mwh: float = 150
    
    start_time: datetime
    end_time: datetime
        
settings = Settings()