from inspect import stack
from typing import Any, Optional

import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import Page
from playwright.sync_api._generated import Locator
from selenium.common.exceptions import ElementNotInteractableException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from config import conf_obj


class CustomPage:  # type: ignore
    def __init__(self, original: Page):
        self.original = original

    def set_window(self) -> None:
        """
        Navigate to url and maximize window
        """

        self.original.goto(conf_obj.GLOBAL_URL + conf_obj.LOGIN_URL)

    def get_element(
        self, locator: str, highlight: bool = True, clickable: bool = True
    ) -> Optional[Locator]:  # type: ignore
        try:
            # Highlight element for better debugging
            if highlight:
                self.original.locator(locator).highlight()

            return self.original.locator(locator)
        # Not intractable element exception
        except ElementNotInteractableException:
            return self.original.locator(locator)
        # Timeout exception
        except TimeoutException:
            self.c_assert(False)
            return None

    def safe_send_keys(self, locator: str, input_text: str) -> None:
        """
        :param locator:
        :param input_text:
        """
        self.get_element(locator).click()
        action: ActionChains = ActionChains(self)
        action.send_keys(input_text)
        action.perform()

    def select_from_dropdown_by_value(self, locator: str, dropdown_menu: str) -> None:
        # Used for dropdown by value
        select: Select = Select(self.get_element(locator))
        select.select_by_value(dropdown_menu)

    def check_if_element_exists(self, locator: str, time_to_wait: int = 5) -> bool:
        """
        Validate if element exists on page.
        Mostly used in validation
        :param locator:
        :param time_to_wait: time to wait for element to load
        :return: True/False
        """
        try:
            self.get_element(locator).is_visible(timeout=time_to_wait)
        except TimeoutException:
            return False
        return True

    def hover_element(self, locator: str) -> None:
        """
        # Hover over the element
        :param locator:
        """
        element: Locator = self.get_element(locator)
        hov: ActionChains = ActionChains(self).move_to_element(to_element=element)
        hov.perform()

    def wait_for_loader_to_load(self, locator: str, time_to_wait: int = 20) -> None:
        """
        Wait for loading element to appear
        required to prevent prematurely checking if element
        has disappeared, before it has had a chance to appear
        """
        try:
            self.get_element(locator).is_visible(timeout=time_to_wait)
            self.get_element(locator).is_hidden(timeout=time_to_wait)

        except TimeoutException:
            # if timeout exception was raised - it may be safe to
            # assume loading has finished, however this may not
            # always be the case, use with caution, otherwise handle
            # appropriately.
            assert False, "wait_for_loader_to_load(): TimeoutException"

    def take_screenshot(self) -> None:
        """
        Take screenshot and save it to reports/screenshot/current_date folder
        """
        function_stack = stack()[2]  # Fetch name of function assertion occurs in

        # Print SS with name that match: function_where_assertion_occurs()_assertion_line_in_that_funtion.png
        screenshot_name: str = f"{function_stack[3]}()_line_{function_stack[2]}.png"
        self.original.screenshot(path=conf_obj.SCREENSHOT_PATH + "/" + screenshot_name)
        # Attach screenshot to allure
        self.attach_allure_png()

    def attach_allure_png(self) -> None:
        allure.attach(
            self.original.screenshot(),
            name="Screenshot",
            attachment_type=AttachmentType.PNG,
        )

    def c_assert(self, value1: Any, value2: Any = True) -> None:
        """
        Custom assert that compares two values and if false then:
        - take screenshot on fail
        - print message with file, function and lines assertion occurs
        """
        # If assert condition is not met take screenshot
        function_stack = stack()[2]
        assert_stack = stack()[1]  #

        message = (
            f"In file '{assert_stack[1]}'\n"
            f"function: '{function_stack[3]}()': line = {function_stack[2]}\n"
            f"Assertion on line {assert_stack[2]}: \n"
            f"Value is :'{value1}' instead of '{value2}'"
        )
        try:
            assert value1 == value2
        except AssertionError:
            self.take_screenshot()
        finally:
            assert value1 == value2, message
