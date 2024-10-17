import faker
import string
import random


def get_random_data_user():
    fake = faker.Faker('en_US')
    email = fake.email()
    password = fake.password()
    name = fake.first_name()
    return email, password, name


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

