from typing import Generator

from lovely.pytest.docker.compose import Services
from playwright.sync_api import Browser, BrowserType, Playwright, sync_playwright
from playwright.sync_api._generated import BrowserContext
from pytest import fixture

from config import conf_obj, get_browser
from src.page import CustomPage
from src.pom.login import LoginPage


@fixture(scope="session", autouse=True)
async def docker_juice_shop(docker_services: Services) -> None:
    test_db_service_name: str = "juice-shop"
    docker_services.start(test_db_service_name)
    docker_services.wait_for_service(test_db_service_name, 3000, timeout=60)


@fixture(scope="session")
def browser() -> Browser:
    browser: Playwright = sync_playwright().start()
    browser_info: dict = get_browser()
    launcher: BrowserType = getattr(browser, browser_info["browser"])
    return launcher.launch(
        headless=not conf_obj.LOCAL, channel=browser_info.get("channel")
    )


@fixture(scope="session")
def context(browser) -> Generator[BrowserContext, None, None]:
    context = browser.new_context()
    # Turn on the recording
    # context = browser.new_context(record_video_dir="records")
    # context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context
    # context.tracing.stop(path="reports/trace.zip")
    # context.storage_state(path="reports/storage.txt")
    context.close()


@fixture(scope="session")
def page(context) -> CustomPage:
    # Record video
    return CustomPage(context.new_page())


@fixture(scope="session")
def successful_login(page: CustomPage) -> None:
    login_page: LoginPage = LoginPage(page)
    login_page.navigate_to_homepage()
    login_page.login_to_application(conf_obj.LOGIN_USERNAME, conf_obj.LOGIN_PASSWORD)
