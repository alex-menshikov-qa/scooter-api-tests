# Scooter API Tests

API test automation project for a courier and order management service.

## Tech stack

* Python
* Pytest
* Requests
* Allure

## Test coverage

* Courier creation
* Courier login
* Order creation
* Order list retrieval

## Project structure

* `tests/` - API test cases
* `conftest.py` - shared fixtures
* `data.py` - test data and configuration
* `pytest.ini` - Pytest configuration
* `requirements.txt` - project dependencies

## How to run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest
```

Run tests with Allure results:

```bash
pytest --alluredir=allure_results
allure serve allure_results
```

## Notes

This repository is a portfolio version of an API testing project. It demonstrates test design, API coverage, Pytest fixtures, and structured test organization.