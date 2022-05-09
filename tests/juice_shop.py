import allure
from src.pom.add_apple_juice import AddAppleJuicePage
from src.pom.add_apple_pomice import AddApplePomicePage


def test_add_apple_juice(page, successful_login) -> None:
    add_apple_juice: AddAppleJuicePage = AddAppleJuicePage(page)

    add_apple_juice.add_apple_juice_to_basket()
    add_apple_juice.validate_apple_juice_in_basket()


"""

def test_validate_banana_description(page, successful_login):
    # Click text=Banana Juice (1000ml)
    page.locator("text=Banana Juice (1000ml)").click()
    # Click text=Monkeys love it the most.
    assert page.locator("text=Monkeys love it the most.")
    # Click [aria-label="Close\ Dialog"]
    page.locator("[aria-label=\"Close\\ Dialog\"]").click()

"""


def test_add_apple_pomace(page, successful_login):
    apple_pomice_page: AddApplePomicePage = AddApplePomicePage(page)
    apple_pomice_page.add_apple_pomice_to_basket()
    apple_pomice_page.validate_apple_pomice()


def test_fail_on_purpose(page, successful_login):
    # Click text=Monkeys love it the most.
    @allure.step
    def fail_test() -> None:
        assert page.locator("text=Moose love it the most.").is_visible(), f"Element not visible on page"

    fail_test()
