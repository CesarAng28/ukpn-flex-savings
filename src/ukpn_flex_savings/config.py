from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    ukpn_dispatch_url: str
    ukpn_api_key: str
    default_flex_price_gbp_per_mwh: float = 150
        
settings = Settings()