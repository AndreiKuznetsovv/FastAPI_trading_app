from pydantic_settings import BaseSettings, SettingsConfigDict

"""Global App configuration"""


class Settings(BaseSettings):
    MODE: str
    # DB variables
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    # fastapi_users SECRET for JWt
    SECRET: str
    # Celery Settings
    EMAIL_USER: str
    EMAIL_PASS: str

    @property
    def DB_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".test.env")


settings = Settings()
