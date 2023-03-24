import os

from playwright.async_api import BrowserContext
from pytest_asyncio import fixture

from config import conf_obj
from constants import SessionConstants
from src.pom.login import LoginPage


@fixture(scope="function", autouse=True)
async def register_and_login(
    login: LoginPage,
    context: BrowserContext,
) -> None:
    if os.path.exists(SessionConstants.STORAGE_STATE):
        return

    await login.navigate_to_homepage()
    await login.register(conf_obj.LOGIN_USERNAME, conf_obj.LOGIN_PASSWORD, conf_obj.SECURITY_ANSWER)
    await login.validate_successful_registration()
    await login.application_login(conf_obj.LOGIN_USERNAME, conf_obj.LOGIN_PASSWORD)
    await context.storage_state(path=SessionConstants.STORAGE_STATE)
