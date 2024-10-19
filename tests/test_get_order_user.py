"""
Получение заказов конкретного пользователя:
- авторизованный пользователь,
- неавторизованный пользователь.
"""

import pytest
import requests
import allure
from src.config import Config
import json
from src.data import get_ingredients


class TestGetOrderUser:
    @allure.title("Получение заказов конкретного пользователя")
    @allure.step("Получение заказов авторизованного пользователя")
    def test_get_order_authorise_user(self, create_and_delete_user, create_order_with_ingredients):
        token = create_and_delete_user["token"]
        headers = {"Authorization": token}
        get_order_response = requests.get(f"{Config.URL}api/orders", headers=headers)
        assert get_order_response.status_code == 200
        get_order_response_json = get_order_response.json()
        assert get_order_response_json["success"] is True
        assert "orders" in get_order_response_json

    @allure.step("Получение заказов неавторизованного пользователя")
    def test_get_order_authorise_user(self, create_and_delete_user, create_order_with_ingredients):
        get_order_response = requests.get(f"{Config.URL}api/orders")
        assert get_order_response.status_code == 401
        get_order_response_json = get_order_response.json()
        assert get_order_response_json["success"] is False
        assert get_order_response_json["message"] == "You should be authorised"


