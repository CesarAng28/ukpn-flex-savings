from enum import Enum

class TechnologyType(Enum):
    BATTERY = "Battery"
    ELECTRIC_VEHICLE = "Electric Vehicle"
    HEAT_PUMP = "Heat Pump"
    OTHER = "Other"
    
class FlexibilityType(Enum):
    DEMAND_TURN_DOWN = "demand_turn_down"
    DEMAND_TURN_UP = "demand_turn_up"
    GENERATION_TURN_DOWN = "generation_turn_down"
    GENERATION_TURN_UP = "generation_turn_up"