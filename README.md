# PlayWrightAutomation

## First of all

Project is run on juice-shop.herokuapp app. If you want to run web page set `GLOBAL_URL` to juice-shop.herokuapp.com
Juice-shop.herokuapp can be run locally. In order to run it locally run `docker-compose up juice-shop`
It is recommended to do registration first:

    pytest -s -v tests/registration.py # Run tests

Run tests with PlayWright framework. PlayWright project supports different browsers.
By changing `.env` file user can set: `chrome`, `firefox`, `safari` or `edge` browser.
Project supports running files with docker in headless browser with make.


## Setup

Copy `.env.example` to `.env` and fill in the variables.

Install `pre-commit`:

    pip install pre-commit
    pre-commit install --install-hooks

## Usage

Install dependencies:

    pip-compile -r requirements.in
    pip install -r requirements.txt

Run tests examples:

    pytest -s -v tests/juice_shop.py # Run tests

Run test and generate allure report:

    pytest -s -v tests/juice_shop.py --alluredir=reports/allure-results  
    allure serve allure/results

Run tests with docker:

    make compose-test
    make compose-test-allure

### Code formatting

Project use [black](https://github.com/ambv/black/) to format the python files.

Install and run `black`, `isort`, `mypy`:

    pip install black
    black .
    pip install isort
    isort .
    pip install mypy
    mypy .
