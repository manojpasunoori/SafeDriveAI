from fastapi import APIRouter
from app.schemas.predict import PredictIn, PredictOut
from app.services.weather import weather_client
from app.services.risk import compute_risk

router = APIRouter(prefix="/v1", tags=["predict"])

@router.post("/predict", response_model=PredictOut)
async def predict(payload: PredictIn) -> PredictOut:
    wx = await weather_client.current(payload.location.lat, payload.location.lon)
    temp_c = float(wx["main"]["temp"])
    precipitation = float(wx.get("rain", {}).get("1h", 0.0))
    visibility_km = float(wx.get("visibility", 10000)) / 1000.0
    score, feats = compute_risk(
        temp_c=temp_c,
        precipitation_mmhr=precipitation,
        visibility_km=visibility_km,
        hour=payload.hour,
    )
    return PredictOut(risk_score=score, features=feats)
