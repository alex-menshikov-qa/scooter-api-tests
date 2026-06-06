import pytest
import requests
import allure


@allure.suite("Courier Creation Tests")
@allure.title("Test Create Courier")
class TestCreateCourier:

    @allure.step("Test successful courier registration")
    def test_create_courier_successfully(self, setup_and_teardown):
        payload, response, courier_id = setup_and_teardown
        assert response.status_code == 201, "Expected status code 201 for successful registration"
        assert response.json() == {"ok": True}, "Response should be {'ok': True}"

    @pytest.mark.xfailed
    @allure.step("Test duplicate courier registration")
    def test_create_duplicate_courier(self, register_new_courier, setup_and_teardown):
        payload, response, courier_id = setup_and_teardown
        duplicate_payload, duplicate_response = register_new_courier(payload)
        assert duplicate_response.json()['message'] == "Этот логин уже используется"

    @allure.step("Test courier creation without some required fields")
    def test_create_courier_without_required_fields(self, generate_user_data, config):
        url = f"{config}/api/v1/courier"
        payload = {
            "password": generate_user_data['password'],
            "firstName": generate_user_data['first_name']
        }

        response = requests.post(url, json=payload)
        assert response.status_code == 400, "Expected status code 400 for missing login"
        assert response.json()['message'] == "Недостаточно данных для создания учетной записи"

    @allure.step("Test successful request returns 'ok:true'")
    def test_successful_request_ok_true(self, setup_and_teardown):
        payload, response, courier_id = setup_and_teardown

        assert response.json() == {"ok": True}, "Response should be {'ok': True}"

    @allure.step("Test courier creation without login")
    def test_create_courier_without_login(self, generate_user_data, config):
        url = f"{config}/api/v1/courier"
        payload = {
            "password": generate_user_data['password'],
            "firstName": generate_user_data['first_name']
        }

        response = requests.post(url, json=payload)
        assert response.status_code == 400, "Expected status code 400 for missing login"

    @allure.step("Test courier creation without password")
    def test_create_courier_without_password(self, generate_user_data, config):
        url = f"{config}/api/v1/courier"
        payload = {
            "login": generate_user_data['login'],
            "firstName": generate_user_data['first_name']
        }

        response = requests.post(url, json=payload)
        assert response.status_code == 400, "Expected status code 400 for missing password"

    @pytest.mark.xfailed
    @allure.step("Test courier creation without first name")
    def test_create_courier_without_first_name(self, generate_user_data, config):
        url = f"{config}/api/v1/courier"
        payload = {
            "login": generate_user_data['login'],
            "password": generate_user_data['password'],
        }

        response = requests.post(url, json=payload)
        assert response.status_code == 400, "Expected status code 400 for missing first name"

    @allure.step("Test courier with existent login")
    def test_create_courier_existent_login(self, register_new_courier, setup_and_teardown):
        payload, response, courier_id = setup_and_teardown
        duplicate_payload, duplicate_response = register_new_courier(payload)
        assert duplicate_response.status_code == 409, "Expected status code 409 for existent login name"
