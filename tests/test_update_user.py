"""
Изменение данных пользователя:
- с авторизацией,
- без авторизации,
Для обеих ситуаций нужно проверить, что любое поле можно изменить.
Для неавторизованного пользователя — ещё и то, что система вернёт ошибку.
"""
import pytest
import requests
import allure
from src.config import Config
import json
from src.helpers import get_random_data_user
from src.helpers import generate_random_name, generate_random_email, generate_random_password


class TestUpdateUser:

    @allure.title("Изменение данных пользователя")
    @allure.step("Изменение всех данных пользователя с авторизацией")
    def test_update_user_all_date_with_authorise(self, create_and_delete_user):
        token = create_and_delete_user["token"]
        new_email, new_password, new_name = get_random_data_user()
        new_user_data = {
            "email": new_email,
            "password": new_password,
            "name": new_name
        }
        headers = {"Authorization": token}
        update_user_response = requests.patch(f"{Config.URL}api/auth/user", json=new_user_data, headers=headers)
        assert update_user_response.status_code == 200
        update_user_response_json = update_user_response.json()
        assert update_user_response_json["success"] is True
        assert update_user_response_json["user"]["email"] == new_user_data["email"]
        assert update_user_response_json["user"]["name"] == new_user_data["name"]

    @allure.step("Изменение поля email с авторизацией")
    def test_update_user_email_with_authorise(self, create_and_delete_user):
        token = create_and_delete_user["token"]
        user_data = create_and_delete_user["user_data"]
        new_user_data = {
            "email": generate_random_email()
        }
        headers = {"Authorization": token}
        update_user_response = requests.patch(f"{Config.URL}api/auth/user", json=new_user_data, headers=headers)
        assert update_user_response.status_code == 200
        update_user_response_json = update_user_response.json()
        assert update_user_response_json["success"] is True
        assert update_user_response_json["user"]["email"] == new_user_data["email"]
        assert update_user_response_json["user"]["name"] == user_data["name"]

    @allure.step("Изменение поля name с авторизацией")
    def test_update_user_name_with_authorise(self, create_and_delete_user):
        token = create_and_delete_user["token"]
        user_data = create_and_delete_user["user_data"]
        new_user_data = {
            "name": generate_random_name()
        }
        headers = {"Authorization": token}
        update_user_response = requests.patch(f"{Config.URL}api/auth/user", json=new_user_data, headers=headers)
        assert update_user_response.status_code == 200
        update_user_response_json = update_user_response.json()
        assert update_user_response_json["success"] is True
        assert update_user_response_json["user"]["email"] == user_data["email"]
        assert update_user_response_json["user"]["name"] == new_user_data["name"]

    @allure.step("Изменение поля password с авторизацией")
    def test_update_user_password_with_authorise(self, create_and_delete_user):
        token = create_and_delete_user["token"]
        user_data = create_and_delete_user["user_data"]
        new_user_data = {
            "password": generate_random_password()
        }
        headers = {"Authorization": token}
        update_user_response = requests.patch(f"{Config.URL}api/auth/user", json=new_user_data, headers=headers)
        assert update_user_response.status_code == 200
        update_user_response_json = update_user_response.json()
        assert update_user_response_json["success"] is True
        assert update_user_response_json["user"]["email"] == user_data["email"]
        assert update_user_response_json["user"]["name"] == user_data["name"]

    @allure.step("Изменение данных пользователя без авторизации")
    def test_update_user_without_authorise(self, create_and_delete_user):
        new_email, new_password, new_name = get_random_data_user()
        new_user_data = {
            "email": new_email,
            "password": new_password,
            "name": new_name
        }
        update_user_response = requests.patch(f"{Config.URL}api/auth/user", json=new_user_data)
        assert update_user_response.status_code == 401
        assert update_user_response.json()["success"] is False
        assert update_user_response.json()["message"] == "You should be authorised"















