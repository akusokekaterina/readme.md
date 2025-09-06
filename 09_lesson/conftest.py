import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Данные для подключения к вашей базе данных
DB_CONNECTION_STRING = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"


@pytest.fixture(scope="session")
def db_engine():
    """Фикстура для создания engine."""
    engine = create_engine(DB_CONNECTION_STRING)
    yield engine
    engine.dispose()


@pytest.fixture
def db_session(db_engine):
    """Фикстура для сессии базы данных."""
    SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=db_engine
    )
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
