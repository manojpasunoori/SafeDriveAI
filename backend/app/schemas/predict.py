from pydantic import BaseModel, Field
from .common import Location

class PredictIn(BaseModel):
    location: Location
    hour: int = Field(..., ge=0, le=23)

class PredictOut(BaseModel):
    risk_score: float
    features: dict
