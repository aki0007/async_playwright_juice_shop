from playwright.async_api import Page
from playwright.async_api._generated import BrowserContext
from pytest_asyncio import fixture

from src.pom.login import LoginPage
from src.pom.score_board import ScoreBoardPage

pytest_plugins: list = ["tests.fixtures.playwright"]


@fixture(scope="function")
async def login(page: Page, context: BrowserContext) -> LoginPage:
    yield LoginPage(page)


@fixture(scope="function")
async def score_board(page: Page, context: BrowserContext) -> ScoreBoardPage:
    yield ScoreBoardPage(page)
