from typing import AsyncGenerator

from playwright.async_api import Page
from playwright.async_api._generated import APIRequestContext
from pytest_asyncio import fixture

from src.pom.api import AsyncAPI
from src.pom.chat_bot import ChatBotPage
from src.pom.contact import ContactPage
from src.pom.login import LoginPage
from src.pom.navigation import NavigationPage
from src.pom.photo_wall import PhotoWallPage
from src.pom.score_board import ScoreBoardPage

pytest_plugins: list = ["tests.fixtures.playwright"]


@fixture(scope="function")
async def login(page: Page) -> AsyncGenerator[LoginPage, None]:
    yield LoginPage(page)


@fixture(scope="function")
async def score_board(page: Page) -> AsyncGenerator[ScoreBoardPage, None]:
    yield ScoreBoardPage(page)


@fixture(scope="function")
async def navigation(page: Page) -> AsyncGenerator[NavigationPage, None]:
    yield NavigationPage(page)


@fixture(scope="function")
async def chatbot(page: Page) -> AsyncGenerator[ChatBotPage, None]:
    yield ChatBotPage(page)


@fixture(scope="function")
async def async_api(api_request: APIRequestContext) -> AsyncGenerator[AsyncAPI, None]:
    yield AsyncAPI(api_request)


@fixture(scope="function")
async def photo_wall(page: Page) -> AsyncGenerator[PhotoWallPage, None]:
    yield PhotoWallPage(page)


@fixture(scope="function")
async def contact(page: Page, api_request: APIRequestContext) -> AsyncGenerator[ContactPage, None]:
    yield ContactPage(page, api_request)
