"""
Создание заказа:
- с авторизацией,
- без авторизации,
- с ингредиентами,
- без ингредиентов,
- с неверным хешем ингредиентов.
"""

import pytest
import requests
import allure
from src.config import Config
import json
from src.data import get_ingredients, list_invalid_ingredients


class TestCreateOrder:
    @allure.title("Создание заказа")
    @allure.step("Создание заказа с авторизацией с ингредиентами")
    def test_create_order_with_ingredients_with_authorise(self, create_and_delete_user, login_user):
        token = create_and_delete_user["token"]
        headers = {"Authorization": token}
        ingredients = {"ingredients": get_ingredients()[:2]}
        create_order_response = requests.post(f"{Config.URL}api/orders", json=ingredients, headers=headers)
        assert create_order_response.status_code == 200
        create_order_response_json = create_order_response.json()
        assert create_order_response_json["success"] is True
        assert create_order_response_json["name"] == "Бессмертный флюоресцентный бургер"
        assert len(create_order_response_json["order"]["ingredients"]) == 2
        assert create_order_response_json["order"]["status"] == 'done'

    @allure.step("Создание заказа с авторизацией без ингредиентов")
    def test_create_order_without_ingredients_with_authorise(self, create_and_delete_user, login_user):
        token = create_and_delete_user["token"]
        headers = {"Authorization": token}
        create_order_response = requests.post(f"{Config.URL}api/orders", headers=headers)
        assert create_order_response.status_code == 400
        create_order_response_json = create_order_response.json()
        assert create_order_response_json["success"] is False
        assert create_order_response_json["message"] == "Ingredient ids must be provided"

    @allure.step("Создание заказа без авторизации с ингредиентами")
    def test_create_order_with_ingredients_without_authorise(self, create_and_delete_user, login_user):
        ingredients = {"ingredients": get_ingredients()[:2]}
        create_order_response = requests.post(f"{Config.URL}api/orders", json=ingredients)
        assert create_order_response.status_code == 200
        create_order_response_json = create_order_response.json()
        assert create_order_response_json["success"] is True
        assert create_order_response_json["name"] == "Бессмертный флюоресцентный бургер"
        assert "status" not in create_order_response_json["order"]
        assert "ingredients" not in create_order_response_json["order"]
        assert "order" in create_order_response_json
        assert create_order_response_json["order"]["number"] is not None

    @allure.step("Создание заказа без авторизации без ингредиентов")
    def test_create_order_without_ingredients_with_authorise(self, create_and_delete_user, login_user):
        create_order_response = requests.post(f"{Config.URL}api/orders")
        assert create_order_response.status_code == 400
        create_order_response_json = create_order_response.json()
        assert create_order_response_json["success"] is False
        assert create_order_response_json["message"] == "Ingredient ids must be provided"

    @allure.step("Создание заказа c неверным хешем ингредиентов")
    def test_create_order_with_wrong_id_ingredient(self,create_and_delete_user,login_user):
        token = create_and_delete_user["token"]
        headers = {"Authorization": token}
        ingredients = {"ingredients": list_invalid_ingredients}
        create_order_response = requests.post(f"{Config.URL}api/orders", json=ingredients, headers=headers)
        assert create_order_response.status_code == 500





