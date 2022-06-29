from typing import Generator

from lovely.pytest.docker.compose import Services
from playwright.sync_api import Browser, BrowserType, Playwright, sync_playwright
from playwright.sync_api._generated import BrowserContext
from pytest import fixture

from config import conf_obj, get_browser
from src.page import CustomPage
from src.pom.login import LoginPage


@fixture(scope="session", autouse=False)
async def docker_juice_shop(docker_services: Services) -> None:
    test_db_service_name: str = "juice-shop"
    docker_services.start(test_db_service_name)
    docker_services.wait_for_service(test_db_service_name, 3000, timeout=60)


@fixture(scope="session")
def playwright() -> Generator[Playwright, None, None]:
    with sync_playwright() as playwright:
        yield playwright


@fixture(scope="session")
def browser(playwright: Playwright) -> Browser:
    browser_info: dict = get_browser()
    launcher: BrowserType = getattr(playwright, browser_info["browser"])
    return launcher.launch(
        headless=not conf_obj.LOCAL, channel=browser_info.get("channel")
    )


@fixture(scope="function")
def context(
    playwright: Playwright, browser: Browser
) -> Generator[BrowserContext, None, None]:
    # Return context with/without trace depending on config.TRACE bool
    params = {}
    if conf_obj.DEVICES:
        params = {**playwright.devices[conf_obj.DEVICES]}
    if conf_obj.TRACE:
        params["record_video_dir"] = "reports/records"
    context: BrowserContext = browser.new_context(**params)
    if conf_obj.TRACE:
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context
    if conf_obj.TRACE:
        context.tracing.stop(path="reports/reports.zip")
        # Turn on storage if necessary
        # trace_context.storage_state(path="reports/storage.txt")
    context.close()


@fixture(scope="function")
def page(context) -> CustomPage:
    # Record video
    return CustomPage(context.new_page())


@fixture(scope="function")
def successful_login(page: CustomPage) -> None:
    login_page: LoginPage = LoginPage(page)
    login_page.navigate_to_homepage()
    login_page.login_to_application(conf_obj.LOGIN_USERNAME, conf_obj.LOGIN_PASSWORD)


@fixture(scope="function")
def turn_on_trace() -> Generator[None, None, None]:
    """
    If turn_on_trace fixture is called trace_context will be called instead of context
    In order for trace to work it has to be imported first as fixture in a test case
    """
    conf_obj.TRACE = True
    yield
    conf_obj.TRACE = False
