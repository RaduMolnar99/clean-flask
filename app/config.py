import typing

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_nested_delimiter = "__"
        env_file = ".env"

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: str
    POSTGRES_APPLICATION_NAME: str

    @property
    def sqlalchemy_database_uri(self: typing.Self) -> str:
        db_uri = PostgresDsn.build(
            scheme="postgresql",
            user=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            path=f"/{self.POSTGRES_DB}",
            port=self.POSTGRES_PORT
        )
        return typing.cast(str, db_uri)


settings = Settings()
