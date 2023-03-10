import asyncio
import os
from typing import Generator

from _pytest.fixtures import SubRequest
from playwright.async_api import Playwright, async_playwright, Browser, BrowserType, Page
from playwright.async_api._generated import BrowserContext
from pytest_asyncio import fixture

from config import LOCAL, conf_obj, get_browser
from constants import SessionConstants


@fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()


@fixture(scope="session")
async def playwright() -> Generator[Playwright, None, None]:
    async with async_playwright() as playwright:
        yield playwright


@fixture(scope="session")
async def browser(playwright: Playwright) -> Browser:
    browser_info: dict = get_browser()
    launcher: BrowserType = getattr(playwright, browser_info["browser"])
    browser: Browser = await launcher.launch(headless=not LOCAL, channel=browser_info.get("channel"))
    yield browser


@fixture(scope="function")
async def context(playwright: Playwright, browser: Browser, request: SubRequest) -> BrowserContext:
    # Return context with/without trace depending on config.TRACE bool
    params = {}
    if conf_obj.DEVICES:
        params = {**playwright.devices[conf_obj.DEVICES]}
    if request.node.get_closest_marker("record"):
        params["record_video_dir"] = "report/records"
    # Add storage state to context to avoid un
    if os.path.exists(SessionConstants.STORAGE_STATE):
        params["storage_state"] = SessionConstants.STORAGE_STATE
    context: BrowserContext = await browser.new_context(**params)
    if request.node.get_closest_marker("record"):
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        SessionConstants.TEST_NAME = os.environ.get("PYTEST_CURRENT_TEST", "test").split(":")[-1].split(" ")[0]

    yield context
    if SessionConstants.TRACE:
        await context.tracing.stop(path=f"report/{SessionConstants.TEST_NAME}.zip")
        # Turn on storage if necessary
        # trace_context.storage_state(path="report/storage.txt")
    await context.close()


@fixture(scope="function")
async def page(context: BrowserContext) -> Page:
    # Record video
    page: Page = await context.new_page()
    page.set_default_timeout(SessionConstants.DEFAULT_TIMEOUT)
    yield page
    await page.close()
