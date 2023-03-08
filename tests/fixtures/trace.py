
from logging import Logger
from typing import Generator

import allure
from _pytest.fixtures import SubRequest
from allure_commons.types import AttachmentType
from playwright.sync_api import Page
from pytest import FixtureRequest, fixture

from config import conf_obj
from constants import SessionConstants


@fixture(scope="function")
def turn_on_trace() -> Generator[None, None, None]:
    """
    If turn_on_trace fixture is called trace_context will be called instead of context
    In order for trace to work it has to be imported first as fixture in a test case
    """
    conf_obj.TRACE = True
    yield
    conf_obj.TRACE = False


@fixture(scope="function", autouse=True)
def take_screenshot(request: SubRequest, page: Page) -> Generator[None, None, None]:
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
    screenshot_name: str = (
        f"{SessionConstants.TESTRAIL_C_ID}"
        if SessionConstants.TESTRAIL_C_ID
        else "screenshot"
    )
    page.screenshot(
        path=SessionConstants.SCREENSHOT_PATH + "/" + screenshot_name + ".png"
    )


@fixture(scope="function", autouse=True)
def attach_allure_png(
    request: FixtureRequest, page: Page
) -> Generator[None, None, None]:
    # Add SS to allure if test failed
    yield
    try:
        if request.node.rep_call.passed:
            return
    except AttributeError:
        SessionConstants.TESTRAIL_C_ID = "fixture_screenshot"

    allure.attach(
        page.screenshot(),
        name=f"{SessionConstants.TESTRAIL_C_ID}",
        attachment_type=AttachmentType.PNG,
    )

