import allure

from src.page import CustomPage


class AddAppleJuicePage:
    __CLOSE_DIALOG = '[aria-label="Close\\ Dialog"]'
    __OPEN_APPLE_JUICE_ITEM = (
        'text=Apple Juice (1000ml) 1.99¤Add to Basket >> [aria-label="Click\\ for\\ more\\ '
        'information\\ about\\ the\\ product"]'
    )
    __OPEN_REVIEWS = "//span[text()='Reviews']"
    __REVIEW_PRODUCT = '[aria-label="Text\\ field\\ to\\ review\\ a\\ product"]'
    __SEND_REVIEW = '[aria-label="Send\\ the\\ review"]'
    __WRITE_A_REVIEW = "text=Write a review"

    def __init__(self, page) -> None:
        # It is necessary to initialise driver as page class member to implement Webdriver
        self.page: CustomPage = page

    @allure.step
    def add_apple_juice_to_basket(self):
        # Click text=Apple Juice (1000ml) 1.99¤Add to Basket
        self.page.get_element(self.__OPEN_APPLE_JUICE_ITEM).click()
        # Click text=Write a review
        self.page.get_element(self.__WRITE_A_REVIEW).click()
        # Click [aria-label="Text\ field\ to\ review\ a\ product"]
        self.page.get_element(self.__REVIEW_PRODUCT).click()
        # Fill [aria-label="Text\ field\ to\ review\ a\ product"]
        self.page.get_element(self.__REVIEW_PRODUCT).fill("Automated review")
        # Click [aria-label="Send\ the\ review"]
        self.page.get_element(self.__SEND_REVIEW).click()
        # Click [aria-label="Close\ Dialog"]
        self.page.get_element(self.__CLOSE_DIALOG).click()

    @allure.step
    def validate_apple_juice_in_basket(self):
        # Click text=Apple Juice (1000ml) 1.99¤Add to Basket >>
        self.page.get_element(self.__OPEN_APPLE_JUICE_ITEM).click()
        # Click mat-expansion-panel-header[role="button"]:has-text("Reviews")
        self.page.get_element(self.__OPEN_REVIEWS).click()
        # Click [aria-label="Close\ Dialog"]
        self.page.get_element(self.__CLOSE_DIALOG).click()
