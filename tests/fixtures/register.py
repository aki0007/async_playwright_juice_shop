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
    await login.navigate_to_homepage()

    if conf_obj.REGISTERED:
        await login.login_from_registration(conf_obj.LOGIN_USERNAME, conf_obj.LOGIN_PASSWORD)
        return

    await login.register(conf_obj.LOGIN_USERNAME, conf_obj.LOGIN_PASSWORD, conf_obj.SECURITY_ANSWER)
    await login.validate_successful_registration()
    await login.login_from_registration(conf_obj.LOGIN_USERNAME, conf_obj.LOGIN_PASSWORD)
    conf_obj.REGISTERED = True
    await context.storage_state(path=SessionConstants.STORAGE_STATE)
