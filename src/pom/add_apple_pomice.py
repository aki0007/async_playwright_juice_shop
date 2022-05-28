import allure

from config import conf_obj
from src.page import CustomPage


class AddApplePomicePage:
    __ADD_APPLE_POMICE_TO_BASKET: str = (
        'text=Apple Pomace 0.89¤Add to Basket >> [aria-label="Add\\ to\\ Basket"]'
    )
    __ME_WANT_IT: str = "text=Me want it!"
    __SHOW_SHOPPING_CART: str = '[aria-label="Show\\ the\\ shopping\\ cart"]'
    _VALIDATE_APPLE_POMICE: str = "text=Apple Pomace"

    def __init__(self, page) -> None:
        # It is necessary to initialise driver as page class member to implement Webdriver
        self.page: CustomPage = page

    @allure.step
    def add_apple_pomice_to_basket(self):
        # Click text=Me want it!
        self.page.get_element(self.__ME_WANT_IT).click()
        # Click text=Apple Pomace 0.89¤Add to Basket >> [aria-label="Add\ to\ Basket"]
        self.page.get_element(self.__ADD_APPLE_POMICE_TO_BASKET).click()
        # Click [aria-label="Show\ the\ shopping\ cart"]
        self.page.get_element(self.__SHOW_SHOPPING_CART).click()

    @allure.step
    def validate_apple_pomice(self):
        assert (
            self.page.original.url
            == conf_obj.GLOBAL_URL + conf_obj.LOGIN_URL + "#/basket"
        )
        # Click text=Apple Pomace
        assert self.page.get_element(self._VALIDATE_APPLE_POMICE)
