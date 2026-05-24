from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    
    ukpn_dispatch_url: str
    dfault_flex_price_gbp_per_mw: float = 150
    
    class Config:
        env_file = ".env"
        
settings = Settings()