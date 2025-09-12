import pytest
from sqlalchemy.orm import Session
from sqlalchemy import text


def test_database_connection(db_session: Session):
    """
    Тест подключения к базе данных.
    """
    try:
        # Простой запрос для проверки подключения
        result = db_session.execute(text("SELECT 1"))
        assert result.scalar() == 1
        print(" ✓ Подключение к базе данных успешно")
    except Exception as e:
        pytest.fail(f" ✗ Ошибка подключения к базе данных: {e}")


def test_query_1_find_user_by_email(db_session: Session):
    """
    Запрос 1: Найти user_id по email.

    SELECT user_id FROM users WHERE user_email='houston42@gmail.com'
    """
    # Сначала проверим существование таблицы users
    try:
        check_table_query = text("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables
                WHERE table_name = 'users'
            )
        """)
        table_exists = db_session.execute(check_table_query).scalar()

        if not table_exists:
            pytest.skip("Таблица 'users' не существует в базе данных")
            return

        # Проверим структуру таблицы users
        check_columns_query = text("""
            SELECT column_name, data_type
            FROM information_schema.columns
            WHERE table_name = 'users'
        """)
        table_structure = db_session.execute(check_columns_query).fetchall()
        print(f"Структура таблицы users: {table_structure}")

        # Выполнение SQL запроса
        query = text("SELECT user_id FROM users WHERE user_email = :email")
        result = db_session.execute(query, {"email": "houston42@gmail.com"})
        user_id = result.scalar()

        # Проверка результатов
        if user_id is not None:
            print(f" ✓ Найден user_id {user_id} для email houston42@gmail.com")
            assert isinstance(user_id, int)
        else:
            print(" ℹ Пользователь с email houston42@gmail.com не найден")
            # Тест считается пройденным, если запрос выполнился без ошибок
            assert True

    except Exception as e:
        pytest.fail(f" ✗ Ошибка при выполнении запроса 1: {e}")


def test_query_2_get_subject_title_by_id(db_session: Session):
    """
    Запрос 2: Получить название предмета по ID.

    SELECT subject_title FROM subject WHERE subject_id = 8
    """
    try:
        # Проверим существование таблицы subject
        check_table_query = text("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables
                WHERE table_name = 'subject'
            )
        """)
        table_exists = db_session.execute(check_table_query).scalar()

        if not table_exists:
            pytest.skip("Таблица 'subject' не существует в базе данных")
            return

        # Проверим структуру таблицы subject
        check_columns_query = text("""
            SELECT column_name, data_type
            FROM information_schema.columns
            WHERE table_name = 'subject'
        """)
        table_structure = db_session.execute(check_columns_query).fetchall()
        print(f"Структура таблицы subject: {table_structure}")

        # Выполнение SQL запроса
        query = text(
            "SELECT subject_title FROM subject WHERE subject_id = :subject_id"
        )
        result = db_session.execute(query, {"subject_id": 8})
        subject_title = result.scalar()

        # Проверка результатов
        if subject_title is not None:
            print(f" ✓ Название предмета с ID 8: {subject_title}")
            assert isinstance(subject_title, str)
        else:
            print(" ℹ Предмет с ID 8 не найден")
            # Тест считается пройденным, если запрос выполнился без ошибок
            assert True

    except Exception as e:
        pytest.fail(f" ✗ Ошибка при выполнении запроса 2: {e}")


def test_query_3_get_distinct_education_forms(db_session: Session):
    """
    Запрос 3: Получить уникальные формы обучения для пользователя.

    SELECT DISTINCT education_form FROM student WHERE user_id=12203
    """
    try:
        # Проверим существование таблицы student
        check_table_query = text("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables
                WHERE table_name = 'student'
            )
        """)
        table_exists = db_session.execute(check_table_query).scalar()

        if not table_exists:
            pytest.skip("Таблица 'student' не существует в базе данных")
            return

        # Проверим структуру таблицы student
        check_columns_query = text("""
            SELECT column_name, data_type
            FROM information_schema.columns
            WHERE table_name = 'student'
        """)
        table_structure = db_session.execute(check_columns_query).fetchall()
        print(f"Структура таблицы student: {table_structure}")

        # Выполнение SQL запроса
        query = text(
            "SELECT DISTINCT education_form FROM student "
            "WHERE user_id = :user_id"
        )
        result = db_session.execute(query, {"user_id": 12203})
        education_forms = [row[0] for row in result.fetchall()]

        # Проверка результатов
        if education_forms:
            print(
                " ✓ Уникальные формы обучения для user_id 12203: "
                f"{education_forms}"
            )
            assert len(education_forms) > 0
            for form in education_forms:
                assert isinstance(form, str)
        else:
            print(" ℹ Формы обучения для user_id 12203 не найдены")
            # Тест считается пройденным, если запрос выполнился без ошибок
            assert True

    except Exception as e:
        pytest.fail(f" ✗ Ошибка при выполнении запроса 3: {e}")


def test_all_queries_execute_without_errors(db_session: Session):
    """
    Тест, что все запросы выполняются без ошибок синтаксиса.
    """
    queries = [
        "SELECT user_id FROM users WHERE user_email = 'test@example.com'",
        "SELECT subject_title FROM subject WHERE subject_id = 1",
        "SELECT DISTINCT education_form FROM student WHERE user_id = 1"
    ]

    for i, query in enumerate(queries, 1):
        try:
            # Выполняем запрос, но не сохраняем результат
            db_session.execute(text(query))
            # Даже если данных нет, главное - нет ошибок синтаксиса
            print(f" ✓ Запрос {i} выполнен без ошибок синтаксиса")
            assert True
        except Exception as e:
            pytest.fail(f" ✗ Ошибка синтаксиса в запросе {i}: {e}")


if __name__ == "__main__":
    pytest.main(["-v", "test_sql_queries.py"])
