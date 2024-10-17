import faker

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