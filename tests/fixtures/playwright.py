import os
from typing import Generator

from _pytest.fixtures import SubRequest
from playwright.sync_api import Browser, BrowserType, Page, Playwright, sync_playwright
from playwright.sync_api._generated import BrowserContext
from pytest import FixtureRequest, fixture

from config import LOCAL, conf_obj, get_browser
from constants import SessionConstants


@fixture(scope="session")
def playwright() -> Generator[Playwright, None, None]:
    with sync_playwright() as playwright:
        yield playwright


@fixture(scope="session")
def browser(playwright: Playwright) -> Browser:
    browser_info: dict = get_browser()
    launcher: BrowserType = getattr(playwright, browser_info["browser"])
    return launcher.launch(headless=not LOCAL, channel=browser_info.get("channel"))


@fixture(scope="function")
def context(
    playwright: Playwright, browser: Browser, request: SubRequest
) -> Generator[
    BrowserContext, None, None
]:  # Return context with/without trace depending on config.TRACE bool
    params = {}
    if conf_obj.DEVICES:
        params = {**playwright.devices[conf_obj.DEVICES]}
    if request.node.get_closest_marker("record"):
        params["record_video_dir"] = "report/records"
    # Add storage state to context to avoid un
    if os.path.exists(SessionConstants.STORAGE_STATE):
        params["storage_state"] = SessionConstants.STORAGE_STATE
    context: BrowserContext = browser.new_context(**params)
    if request.node.get_closest_marker("record"):
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        SessionConstants.TEST_NAME = (
            os.environ.get("PYTEST_CURRENT_TEST", "test").split(":")[-1].split(" ")[0]
        )

    yield context
    if SessionConstants.TRACE:
        context.tracing.stop(path=f"report/{SessionConstants.TEST_NAME}.zip")
        # Turn on storage if necessary
        # trace_context.storage_state(path="report/storage.txt")
    context.close()


@fixture(scope="function")
def page(
    request: FixtureRequest, context: BrowserContext
) -> Generator[Page, None, None]:
    # Record video
    page: Page = context.new_page()
    page.set_default_timeout(SessionConstants.DEFAULT_TIMEOUT)
    yield page
    page.close()
