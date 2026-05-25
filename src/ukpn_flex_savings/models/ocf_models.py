from pydantic import BaseModel

from datetime import datetime

class OCFEstimates(BaseModel):
    timestamp_utc: datetime
    primary_id: str
    expected_solar_generation_mw: float