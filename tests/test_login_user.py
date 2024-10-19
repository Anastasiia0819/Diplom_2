"""
Логин пользователя:
- логин под существующим пользователем,
- логин с неверным логином и паролем.
"""
import pytest
import requests
import allure
from src.config import Config
import json
from src.helpers import generate_random_email, generate_random_password


class TestLoginUser:
    @allure.title("Логин пользователя")
    @allure.step("логин под существующим пользователем")
    def test_login_user_existing_user(self, create_and_delete_user):
        user_data = create_and_delete_user["user_data"]
        login_data = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
        login_response = requests.post(f"{Config.URL}api/auth/login", json=login_data)
        assert login_response.status_code == 200
        login_response_json = login_response.json()
        assert login_response.json()["success"] is True
        assert login_response_json["user"]["email"] == user_data["email"]
        assert login_response_json["user"]["name"] == user_data["name"]

    @allure.step("логин с неверным логином")
    def test_login_wrong_login(self, create_and_delete_user):
        user_data = create_and_delete_user["user_data"]
        login_data = {
            "email": user_data["email"],
            "password": generate_random_password()
        }
        login_response = requests.post(f"{Config.URL}api/auth/login", json=login_data)
        assert login_response.status_code == 401
        assert login_response.json()["success"] is False
        assert login_response.json()["message"] == "email or password are incorrect"

    @allure.step("логин с неверным паролем")
    def test_login_wrong_password(self, create_and_delete_user):
        user_data = create_and_delete_user["user_data"]
        login_data = {
            "email": generate_random_email(),
            "password": user_data["password"]
        }
        login_response = requests.post(f"{Config.URL}api/auth/login", json=login_data)
        assert login_response.status_code == 401
        assert login_response.json()["success"] is False
        assert login_response.json()["message"] == "email or password are incorrect"





