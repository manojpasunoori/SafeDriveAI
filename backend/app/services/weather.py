import httpx
from loguru import logger
from app.core.settings import settings
from app.core.errors import UpstreamError

class WeatherClient:
    def __init__(self, base_url: str | None = None, api_key: str | None = None):
        self.base_url = base_url or settings.OPENWEATHER_BASE_URL
        self.api_key = api_key or settings.OPENWEATHER_API_KEY

    async def current(self, lat: float, lon: float) -> dict:
        params = {"lat": lat, "lon": lon, "appid": self.api_key, "units": "metric"}
        url = f"{self.base_url}/weather"
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.get(url, params=params)
        if r.status_code != 200:
            logger.error(f"OWM error {r.status_code}: {r.text[:200]}")
            raise UpstreamError("openweather", r.status_code)
        return r.json()

weather_client = WeatherClient()
