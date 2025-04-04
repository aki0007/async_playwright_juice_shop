import asyncio
import os
from typing import Any, AsyncGenerator

from pytest import mark
from _pytest.fixtures import SubRequest
from playwright.async_api import Browser, BrowserType, Page, Playwright, async_playwright
from playwright.async_api._generated import APIRequestContext, BrowserContext
from pytest_asyncio import fixture

import config
from config import conf_obj, get_browser
from constants import SessionConstants


@fixture(scope="session")
@mark.asyncio(scope="session")
def event_loop() -> Any:
    policy: Any = asyncio.get_event_loop_policy()
    loop: Any = policy.new_event_loop()
    yield loop
    loop.close()


@fixture(scope="session")
async def playwright() -> AsyncGenerator[Playwright, None]:
    async with async_playwright() as playwright:
        yield playwright


@fixture(scope="session")
async def browser(playwright: Playwright) -> AsyncGenerator[Browser, None]:
    browser_info: dict = get_browser()
    launcher: BrowserType = getattr(playwright, browser_info["browser"])

    browser: Browser = await launcher.launch(headless=config.LOCAL != 1, channel=browser_info.get("channel"))
    yield browser


@fixture(scope="function")
async def context(playwright: Playwright, browser: Browser, request: SubRequest) -> AsyncGenerator[BrowserContext, None]:
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
async def page(context: BrowserContext) -> AsyncGenerator[Page, None]:
    # Record video
    page: Page = await context.new_page()
    page.set_default_timeout(SessionConstants.DEFAULT_TIMEOUT)
    yield page
    await page.close()


@fixture(scope="function")
async def api_request(context: BrowserContext) -> AsyncGenerator[APIRequestContext, None]:
    yield context.request
