import allure
import time

from base.enums import HomeTab, NavigationTab


class GenerateUserPage(object):
    def __init__(self, driver) -> None:
        # It is necessary to initialise driver as page class member to implement Webdriver
        self.page: WebDriver = driver