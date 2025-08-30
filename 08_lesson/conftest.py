import pytest
import os


@pytest.fixture(scope="session")
def base_url():
    return "https://ru.yougile.com"


@pytest.fixture(scope="session")
def auth_headers():
    """Фикстура для заголовков авторизации"""
    token = os.getenv(
        "API_TOKEN") or "your_auth_token_here"  # Токен
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
