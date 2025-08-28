from enum import Enum  # Для режимов (dev/prod/test) — перечисление.

from typing import Any  # Для типов в функциях.

from environs import Env  # Для чтения .env.

from pydantic import PostgresDsn, field_validator  # Для валидации URI БД.

from pydantic_core.core_schema import FieldValidationInfo  # Для валидатора.

from pydantic_settings import BaseSettings  # Базовый класс настроек.

# Создаём Env и читаем .env — настройки берутся оттуда, если есть, иначе дефолты.
env = Env()
env.read_env()


class ModeEnum(str, Enum):
    development = "development"
    production = "production"
    testing = "testing"


class Settings(BaseSettings):
    DATABASE_USER: str = "postgres"
    DATABASE_PASSWORD: str = "DvpR_O!{+4BN#/"
    DATABASE_HOST: str = "127.0.0.1"
    DATABASE_PORT: int = 5432
    DATABASE_NAME: str = "turbo_backend_service_db"

    ASYNC_DATABASE_URI: PostgresDsn | None = None

    @field_validator("ASYNC_DATABASE_URI", mode="after")
    def assemble_db_connection(cls, v: str | None, info: FieldValidationInfo) -> Any:
        if not v:
            return PostgresDsn.build(
                scheme="postgresql+asyncpg",
                username=info.data["DATABASE_USER"],
                password=info.data["DATABASE_PASSWORD"],
                host=info.data["DATABASE_HOST"],
                port=info.data["DATABASE_PORT"],
                path=f'/{info.data["DATABASE_NAME"]}',
            )
        return v


settings = Settings()


class TestSettings(BaseSettings):
    DATABASE_USER: str = "postgres"
    DATABASE_PASSWORD: str = "DvpR_O!{+4BN#/"
    DATABASE_HOST: str = "127.0.0.1"
    DATABASE_PORT: int = 5432
    # Для тестов — с _test.
    DATABASE_NAME: str = "turbo_backend_service_db_test"

    ASYNC_DATABASE_URI: PostgresDsn | None = None

    @field_validator("ASYNC_DATABASE_URI", mode="after")
    def assemble_db_connection(cls, v: str | None, info: FieldValidationInfo) -> Any:
        if not v:
            return PostgresDsn.build(
                scheme="postgresql+asyncpg",
                username=info.data["DATABASE_USER"],
                password=info.data["DATABASE_PASSWORD"],
                host=info.data["DATABASE_HOST"],
                port=info.data["DATABASE_PORT"],
                path=f'/{info.data["DATABASE_NAME"]}',
            )
        return v


test_settings = TestSettings()
