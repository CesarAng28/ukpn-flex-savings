from datetime import datetime

from pydantic import BaseModel

from ukpn_flex_savings.models import flex_types

class FlexDispatches(BaseModel):
    zone: str
    product: str
    start_time_local: datetime
    end_time_local: datetime
    utilisation_mw: float
    technology: str
    dispatch_type: flex_types.FlexDispatchType
    hours_requested: float
    time: datetime
    
    
    