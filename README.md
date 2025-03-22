# United Platform Testing

## Precondition
Install `python3.11`

## Virtual environment
Create virtual environment:

    python3 -m venv venv 
    source venv/bin/activate

## Setup

Copy `.env.example` to `.env` and fill in the variables.

Install `pre-commit`:

    pip install pre-commit
    pre-commit install --install-hooks

## Dependencies

Install dependencies and update them

    pip install -r requirements/dev.txt --no-cache-dir
    pip-compile-multi

NOTE: If pip-compile-multi fails check if program kicked you out of venv. 


Install Playwright:

    playwright install


## Usage

Connect to VPN and run tests with:

    pytest -s -v  # Run all behave tests
    pytest -s -v -m login  # Run login.feature tests
    pytest tests/tests_lvl_1.py::TestLevel1::test_score_board

Run tests and generate allure report

    pytest tests/gui_tests/tests_and_steps/tests_login.py -s -v --alluredir=report/allure-report 
    allure serve allure/report

### MakeFile
Run tests with docker using `MakeFile`.

    make compose-test  # Run python tests
    make compose-test-allure  # Run tests and create allure-repors
    make composet-test-allure args='--create_rfp' # Set any argument in args=''

MakeFile run tests in browser in headless mode by setting environment variable `LOCAL=0`

### Environment
Project support different environment variables that can be found in `.env.example`
`BROWSER`: chrome, firefox, safari, edge
`DEVICES`: mobile
`ENVIRONMENT`: staging, production, pypi23, development


### Code formatting
Project follows `pep8` convention. More details can be found in `pyproject.toml`
