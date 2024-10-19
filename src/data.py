import faker
import requests
from src.config import Config
from src.helpers import generate_random_ingredient

fake = faker.Faker('en_US')
create_user_without_password = {
        "email": fake.email(),
        "password": None,
        "name": fake.first_name()
    }
create_user_without_email = {
        "email": None,
        "password": fake.password(),
        "name": fake.first_name()
    }
create_user_without_name = {
        "email": fake.email(),
        "password": fake.password(),
        "name": None
    }


#получение списка id ингрeдиентов
def get_ingredients():
    response = requests.get(f"{Config.URL}api/ingredients")
    ingredients_json = response.json()
    ingredient_ids = [ingredient['_id'] for ingredient in ingredients_json["data"]]
    return ingredient_ids


list_invalid_ingredients = [get_ingredients()[0], generate_random_ingredient()]


