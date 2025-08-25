import os


class Settings:
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://my_database:Xx123321@localhost:5432/my_database_db"
    )


settings = Settings()
