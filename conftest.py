import pytest
import requests
import random
import string
from data import Config


@pytest.fixture
def config():
    return Config.URL


@pytest.fixture
def generate_user_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    return {
        "login": login,
        "password": password,
        "first_name": first_name
    }


@pytest.fixture
def register_new_courier(config, generate_user_data):
    url = f"{config}/api/v1/courier"

    def register(payload=None):
        if payload is None:
            payload = {
                "login": generate_user_data['login'],
                "password": generate_user_data['password'],
                "firstName": generate_user_data['first_name']
            }

        response = requests.post(url, json=payload)
        return payload, response

    return register


@pytest.fixture
def delete_courier(config):
    url = f"{config}/api/v1/courier"

    def delete(payload):
        courier_id = payload.get("id")
        if courier_id:
            response = requests.delete(f"{url}/{courier_id}")
            return response
        return None

    return delete


@pytest.fixture
def login_courier(config):
    url = f"{config}/api/v1/courier/login"

    def login(payload):
        response = requests.post(url, json=payload)
        return response

    return login


@pytest.fixture(autouse=True)
def setup_and_teardown(register_new_courier, delete_courier):
    payload, response = register_new_courier()
    courier_id = payload['login']

    yield payload, response, courier_id

    delete_courier({"id": courier_id})
