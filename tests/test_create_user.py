import pytest
import requests
import allure
from src.config import Config
from src.data import create_user_without_email, create_user_without_name, create_user_without_password


class TestCreateUser:
    @allure.title("Создание пользователя")
    @allure.step("Создание пользователя с уникальными данными")
    def test_create_user_unique_user(self, create_and_delete_user):
        user_data = create_and_delete_user["user_data"]
        response_data = create_and_delete_user['response_data']
        token = create_and_delete_user["token"]
        assert token is not None
        assert response_data["success"] is True
        assert "user" in response_data
        assert response_data["user"]["email"] == user_data["email"]
        assert response_data["user"]["name"] == user_data["name"]

    @allure.step("Создание пользователя, который уже зарегистрирован")
    @allure.description("Должен быть код ответа 403 Forbidden")
    def test_create_user_double_user_error(self, create_and_delete_user):
        user_data = create_and_delete_user["user_data"]
        duplicate_response = requests.post(f"{Config.URL}api/auth/register", json=user_data)
        assert duplicate_response.status_code == 403
        duplicate_response_json = duplicate_response.json()
        assert duplicate_response_json["success"] is False
        assert duplicate_response_json["message"] == "User already exists"

    @allure.step("Создание пользователя без email,password,name")
    @pytest.mark.parametrize("create_user_without_field", [create_user_without_password,
                                                           create_user_without_email,
                                                           create_user_without_name])
    def test_create_user_without_email_or_password_or_name(self, create_user_without_field):
        response = requests.post(f"{Config.URL}api/auth/register", json=create_user_without_field)
        assert response.status_code == 403
        response_json = response.json()
        assert response_json["success"] is False
        assert response_json["message"] == "Email, password and name are required fields"














