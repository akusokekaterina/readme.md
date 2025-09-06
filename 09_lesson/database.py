from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base


class DatabaseManager:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

    def create_tables(self):
        """Создание таблиц в базе данных."""
        Base.metadata.create_all(bind=self.engine)

    def get_session(self):
        """Получение сессии для работы с БД."""
        return self.SessionLocal()

    def close_session(self, session):
        """Закрытие сессии."""
        session.close()
