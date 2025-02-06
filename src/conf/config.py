class Config:
    DB_URL = "postgresql+asyncpg://postgres:12345@localhost:5432/contacts"
    JWT_SECRET = "your_secret_key"
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRATION_SECONDS = 3600


config = Config
