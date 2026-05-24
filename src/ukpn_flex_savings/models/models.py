from datetime import datetime

from pydantic import BaseModel

from ukpn_flex_savings.models import flex_types

class FlexDispatch(BaseModel):
    zone: str
    product: str
    start_time: datetime
    end_time: datetime
    utilisation_mw: float
    technology: str
    dispatch_type: flex_types.FlexDispatchType
    hours_requested: float
    time: datetime
    
    
    