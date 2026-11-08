# Scooter API Tests

API test automation project for a courier and order management service.

The project demonstrates REST API testing with Python, pytest, Requests, and Allure: positive and negative paths, status-code and response-body checks, parametrized cases, shared fixtures, and documented discrepancies between the API documentation and the API's actual behavior.

## Tech stack

* Python
* pytest
* Requests
* Allure

## Test suite at a glance

21 tests, including parametrized cases:

| File | Tests | What is covered |
|---|---|---|
| `test_create_courier.py` | 8 | `POST /api/v1/courier`: successful creation (`201`, `{"ok": true}`); duplicate login (`409`, error message); missing login, password, or first name (`400`, error message) |
| `test_courier_login.py` | 7 | `POST /api/v1/courier/login`: successful login (`200`, courier `id` in the response); missing login or password (`400`, error message); invalid credentials and non-existent user (`404`) |
| `test_create_order.py` | 5 | `POST /api/v1/orders`: order creation with every scooter color option (one, both, none) (`201`); `track` number in the response |
| `test_order_list.py` | 1 | `GET /api/v1/orders`: response contains an `orders` list |

## Known API discrepancies

Two tests are marked `xfail`: the API does not behave as its documentation says. The expected result stays in the test, so the discrepancy is visible in every run:

| Test | Documented | Actual |
|---|---|---|
| `test_create_courier_without_first_name` | `400` for a missing first name | `409` |
| `test_login_without_password` | `400` with a validation message | `504` |

## Project structure

* `tests/` - API test cases
* `conftest.py` - shared fixtures: random user data, courier registration, login, and cleanup
* `data.py` - configuration and order test data
* `pytest.ini` - pytest configuration (verbose output, Allure results directory)
* `requirements.txt` - project dependencies
* `.env.example` - environment variables and their default values

## Requirements

* Python 3.10+
* [Allure CLI](https://allurereport.org/docs/install/), only to view reports

## How to run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest
```

Allure results are written to `allure_results/` on every run (set in `pytest.ini`). To open the report:

```bash
allure serve allure_results
```

## Environment

| Variable | Default | Purpose |
|---|---|---|
| `BASE_URL` | `https://qa-scooter.praktikum-services.ru` | Service under test |

Example:

```bash
BASE_URL=https://example.com pytest
```

## Notes

This repository is a portfolio version of an API testing project.

The suite runs against a public demo service that this project does not control, so its availability and behavior may affect results.
