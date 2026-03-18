from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASS: str
    POSTGRES_NAME: str

    @property
    def database_url_asyncpg(self):
        return (f"postgres+asyncpg://"
                f"{self. POSTGRES_USER}:{self. POSTGRES_PASS}@{self. POSTGRES_HOST}"
                f":{self. POSTGRES_PORT}/{self. POSTGRES_NAME}")

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings() # type: ignore[call-arg]
