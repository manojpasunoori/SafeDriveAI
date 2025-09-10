from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    ENV: str = "local"
    LOG_LEVEL: str = "INFO"
    OPENWEATHER_API_KEY: str = ""
    OPENWEATHER_BASE_URL: str = "https://api.openweathermap.org/data/2.5"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
