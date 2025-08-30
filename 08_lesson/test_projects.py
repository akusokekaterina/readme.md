import pytest
import uuid
from projects_client import ProjectsClient


class TestProjects:
    """Тесты для работы с проектами"""

    @pytest.fixture
    def projects_client(self, base_url, auth_headers):
        return ProjectsClient(base_url, auth_headers)

    @pytest.fixture
    def sample_project_data(self):
        """Фикстура с данными для создания проекта"""
        return {
            "title": f"Test Project {uuid.uuid4().hex[:8]}",
            "users": {}
        }

    @pytest.fixture
    def created_project(self, projects_client, sample_project_data):
        """Фикстура создает проект и возвращает его ID"""
        response = projects_client.create_project(sample_project_data)
        assert response.status_code == 201
        project_id = response.json()["id"]
        yield project_id
        # Cleanup - удаляем проект после теста
        projects_client.delete_project(project_id)

    # POSITIVE TESTS

    def test_create_project_positive(
            self, projects_client, sample_project_data):
        """Позитивный тест создания проекта"""
        response = projects_client.create_project(sample_project_data)

        assert response.status_code == 201
        assert "id" in response.json()
        assert isinstance(response.json()["id"], str)

        # Cleanup
        projects_client.delete_project(response.json()["id"])

    def test_get_project_positive(self, projects_client, created_project):
        """Позитивный тест получения проекта"""
        response = projects_client.get_project(created_project)

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == created_project
        assert "title" in data
        assert "timestamp" in data
        assert "users" in data

    def test_update_project_positive(self, projects_client, created_project):
        """Позитивный тест обновления проекта"""
        update_data = {
            "title": "Updated Test Project",
            "users": {"test_user_id": "worker"}
        }

        response = projects_client.update_project(created_project, update_data)

        assert response.status_code == 200
        assert "id" in response.json()

        # Проверяем, что проект действительно обновился
        get_response = projects_client.get_project(created_project)
        assert get_response.json()["title"] == "Updated Test Project"

    # NEGATIVE TESTS

    def test_create_project_negative_missing_title(self, projects_client):
        """Негативный тест создания проекта без обязательного поля title"""
        invalid_data = {
            "users": {}
        }

        response = projects_client.create_project(invalid_data)

        assert response.status_code != 201
        assert response.status_code in [400, 422]  # Ожидаем ошибку валидации

    def test_get_project_negative_not_found(self, projects_client):
        """Негативный тест получения несуществующего проекта"""
        non_existent_id = str(uuid.uuid4())
        response = projects_client.get_project(non_existent_id)

        assert response.status_code == 404

    def test_update_project_negative_invalid_id(self, projects_client):
        """Негативный тест обновления несуществующего проекта"""
        update_data = {
            "title": "Updated Test Project"
        }

        non_existent_id = str(uuid.uuid4())
        response = projects_client.update_project(non_existent_id, update_data)

        assert response.status_code == 404

    def test_update_project_negative_invalid_data(
            self, projects_client, created_project):
        """Негативный тест обновления проекта с невалидными данными"""
        invalid_data = {
            "title": "",  # Пустое название
            "users": {"invalid_user": "invalid_role"}
        }

        response = projects_client.update_project(
            created_project, invalid_data)

        assert response.status_code != 200
        assert response.status_code in [400, 422]
