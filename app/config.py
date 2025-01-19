from pydantic_settings import BaseSettings
from pydantic import model_validator
from dotenv import load_dotenv


load_dotenv()

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DATABASE_URL: str = ""

    @model_validator(mode="after")
    def set_database_url(self):
        # Формируем URL на основе предоставленных данных
        self.DATABASE_URL = (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )
        return self

    class Config:
        env_file = ".env"  # Указываем, откуда брать переменные окружения


# Создаём объект настроек
settings = Settings()

# Выводим сформированный DATABASE_URL
print(settings.DATABASE_URL)