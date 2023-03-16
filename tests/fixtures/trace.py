from typing import Any, AsyncGenerator

import allure
from _pytest.fixtures import SubRequest
from allure_commons.types import AttachmentType
from playwright.async_api import Page
from pluggy._callers import _Result
from pytest import hookimpl
from pytest_asyncio import fixture

from config import conf_obj
from constants import SessionConstants


@hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: str) -> AsyncGenerator[_Result, None, None]:
    # execute all other hooks to obtain the report object
    outcome: _Result = yield
    rep: Any = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


@fixture(scope="function")
async def turn_on_trace() -> AsyncGenerator[None, None, None]:
    """
    If turn_on_trace fixture is called trace_context will be called instead of context
    In order for trace to work it has to be imported first as fixture in a test case
    """
    conf_obj.TRACE = True
    yield
    conf_obj.TRACE = False


@fixture(scope="function", autouse=True)
async def take_screenshot(
    request: SubRequest, page: Page
) -> AsyncGenerator[None, None, None]:
    """
    Take screenshot and save it to report/screenshot/current_date folder
    """
    yield
    try:
        if request.node.rep_call.passed:
            return
    except AttributeError:
        # take_screenshot() uses test TESTRAIL_C_ID for easier SS naming. If test fails before tests are reached,
        # AttributeError occur, and it can be skipped as default screenshot name will be set
        pass

    # Print SS with name that match: function_where_assertion_occurs()_assertion_line_in_that_function.png
    await page.screenshot(
        path=SessionConstants.SCREENSHOT_PATH + "/" + request.node.name + ".png"
    )


@fixture(scope="function", autouse=True)
async def attach_allure_png(
    request: SubRequest, page: Page
) -> AsyncGenerator[None, None, None]:
    # Add SS to allure if test failed
    yield
    allure.attach(
        await page.screenshot(),
        name=request.node.name,
        attachment_type=AttachmentType.PNG,
    )
