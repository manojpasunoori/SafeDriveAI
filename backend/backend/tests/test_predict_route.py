import respx
from httpx import Response
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@respx.mock
def test_predict_v1_happy_path():
    # Mock OpenWeather /weather endpoint
    respx.get("https://api.openweathermap.org/data/2.5/weather").mock(
        return_value=Response(
            200,
            json={
                "main": {"temp": 12.0},
                "rain": {"1h": 2.0},
                "visibility": 4000
            },
        )
    )
    r = client.post("/v1/predict", json={"location": {"lat": 17.385, "lon": 78.4867}, "hour": 18})
    assert r.status_code == 200
    data = r.json()
    assert "risk_score" in data and 0 <= data["risk_score"] <= 1
