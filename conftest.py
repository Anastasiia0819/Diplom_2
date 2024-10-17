import requests
from src.config import Config
import json
from src.helpers import get_random_data_user
import pytest


@pytest.fixture
def create_and_delete_user():
    email, password, name = get_random_data_user()
    user_data = {
        "email": email,
        "password": password,
        "name": name
    }
    #создание пользователя
    create_response = requests.post(f"{Config.URL}api/auth/register", json=user_data)
    assert create_response.status_code == 200, f"Пользователь не был создан, код ответа: {create_response.status_code}, текст: {create_response.text}"

    response_data = create_response.json()

    #получить токен (из ответа создания пользователя)
    token = create_response.json()["accessToken"]
    assert token, f"Токен не был получен: {create_response.text}"

    # передать данные пользователя и токен в тест
    yield {
        "user_data": user_data,
        "response_data": response_data,
        "token": token
    }
    #Удаление пользователя после теста
    headers = {"Authorization": f"Bearer {token}"}
    delete_response = requests.delete(f"{Config.URL}api/auth/user", headers=headers)
    assert delete_response.status_code == 202, f"Ошибка удаления пользователя, статус: {delete_response.status_code}, текст: {delete_response.text}"


