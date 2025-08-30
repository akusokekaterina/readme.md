import requests


class ProjectsClient:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def create_project(self, project_data):
        """Создание проекта"""
        url = f"{self.base_url}/api-v2/projects"
        response = requests.post(url, json=project_data, headers=self.headers)
        return response

    def get_project(self, project_id):
        """Получение проекта по ID"""
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        response = requests.get(url, headers=self.headers)
        return response

    def update_project(self, project_id, update_data):
        """Обновление проекта"""
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        response = requests.put(url, json=update_data, headers=self.headers)
        return response

    def delete_project(self, project_id):
        """Удаление проекта (soft delete)"""
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        delete_data = {"deleted": True}
        response = requests.put(url, json=delete_data, headers=self.headers)
        return response
