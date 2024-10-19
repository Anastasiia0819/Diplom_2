import faker
import string
import random


def get_random_data_user():
    fake = faker.Faker('en_US')
    email = fake.email()
    password = fake.password()
    name = fake.first_name()
    return email, password, name


def generate_random_password(length=6):
    letters = string.ascii_lowercase
    random_password = ''.join(random.choice(letters) for i in range(length))
    return random_password


def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "outlook.com", "example.com"]
    letters = string.ascii_lowercase
    username = ''.join(random.choice(letters) for i in range(8))
    domain = random.choice(domains)
    return f"{username}@{domain}"


def generate_random_name(length=6):
    letters = string.ascii_lowercase
    random_name = ''.join(random.choice(letters) for i in range(length))
    return random_name


