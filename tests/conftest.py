from playwright.sync_api import Browser, Page
from pytest import fixture
from config import get_browser

from config import conf_obj
from src.pom.login import LoginPage


@fixture(scope="session")
def browser() -> Browser:
    return get_browser()


@fixture(scope="session")
def context(browser) -> Browser:
    context = browser.new_context(record_video_dir="records")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    print("tracing started")
    yield context
    context.tracing.stop(path="reports/trace.zip")
    context.storage_state(path="reports/storage.txt")
    context.close()


@fixture(scope="session")
def page(context) -> Page:
    page: Page = context.new_page()
    # Record video
    # page: Page = context.new_page(record_video_dir="records")
    return page


@fixture(scope="session")
def successful_login(page: Page) -> None:
    login_page: LoginPage = LoginPage(page)
    login_page.navigate_to_homepage()
    login_page.login_to_application(conf_obj.LOGIN_USERNAME, conf_obj.LOGIN_PASSWORD)
