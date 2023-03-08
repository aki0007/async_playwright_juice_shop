
from playwright.sync_api import Page
from playwright.sync_api._generated import BrowserContext
from pytest import fixture

from src.pom.login import LoginPage

pytest_plugins: list = ["tests.fixtures.playwright"]


@fixture(scope="function")
def login(page: Page, context: BrowserContext) -> LoginPage:
    return LoginPage(page)
