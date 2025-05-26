from pydantic_settings import BaseSettings
import urllib.parse


class Settings(BaseSettings):
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_DB: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

password = urllib.parse.quote_plus(settings.MYSQL_PASSWORD)

DATABASE_URL = (
    f"mysql+pymysql://{settings.MYSQL_USER}:{password}"
    f"@{settings.MYSQL_HOST}:{settings.MYSQL_PORT}/{settings.MYSQL_DB}")
