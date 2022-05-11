import allure
from playwright.sync_api import Page

from src.pom.add_apple_juice import AddAppleJuicePage
from src.pom.add_apple_pomice import AddApplePomicePage


def test_registration(page: Page) -> None:
    # Leave the test like this to show how codegen creates code
    # Go to http://0.0.0.0:3000/register
    page.goto("http://0.0.0.0:3000/register")
    # Go to http://0.0.0.0:3000/register#/
    page.goto("http://0.0.0.0:3000/register#/")
    # Click [aria-label="Close Welcome Banner"]
    page.locator('[aria-label="Close Welcome Banner"]').click()
    # Click [aria-label="Show\/hide account menu"]
    page.locator('[aria-label="Show\\/hide account menu"]').click()
    # Click button[role="menuitem"]:has-text("exit_to_app Login")
    page.locator('button[role="menuitem"]:has-text("exit_to_app Login")').click()
    # expect(page).to_have_url("http://0.0.0.0:3000/register#/login")
    # Click text=Not yet a customer?
    page.locator("text=Not yet a customer?").click()
    # expect(page).to_have_url("http://0.0.0.0:3000/register#/register")
    # Click [aria-label="Email address field"]
    page.locator('[aria-label="Email address field"]').click()
    # Fill [aria-label="Email address field"]
    page.locator('[aria-label="Email address field"]').fill(
        "jaksa.milanovic007@gmail.com"
    )
    # Click [aria-label="Field for the password"]
    page.locator('[aria-label="Field for the password"]').click()
    # Fill [aria-label="Field for the password"]
    page.locator('[aria-label="Field for the password"]').fill("Test123*")
    # Click [aria-label="Field to confirm the password"]
    page.locator('[aria-label="Field to confirm the password"]').click()
    # Fill [aria-label="Field to confirm the password"]
    page.locator('[aria-label="Field to confirm the password"]').fill("Test123*")
    # Click #registration-form div:has-text("Security Question *") >> nth=3
    page.locator('#registration-form div:has-text("Security Question *")').nth(
        3
    ).click()
    # Click text=Your eldest siblings middle name?
    page.locator("text=Your eldest siblings middle name?").click()
    # Click #registration-form div:has-text("Answer *") >> nth=3
    page.locator('#registration-form div:has-text("Answer *")').nth(3).click()
    # Fill [placeholder="Answer to your security question"]
    page.locator('[placeholder="Answer to your security question"]').fill("Aki")
    # Click [aria-label="Button to complete the registration"]
    # with page.expect_navigation(url="http://0.0.0.0:3000/register#/login"):
    with page.expect_navigation():
        page.locator('[aria-label="Button to complete the registration"]').click()


def test_add_apple_juice(page: Page, successful_login) -> None:
    add_apple_juice: AddAppleJuicePage = AddAppleJuicePage(page)

    add_apple_juice.add_apple_juice_to_basket()
    add_apple_juice.validate_apple_juice_in_basket()


# def test_validate_banana_description(page, successful_login):
#     # Click text=Banana Juice (1000ml)
#     page.locator("text=Banana Juice (1000ml)").click()
#     # Click text=Monkeys love it the most.
#     assert page.locator("text=Monkeys love it the most.")
#     # Click [aria-label="Close\\ Dialog"]
#     page.locator("[aria-label=\"Close\\ Dialog\"]").click()


def test_add_apple_pomace(page: Page, successful_login):
    apple_pomice_page: AddApplePomicePage = AddApplePomicePage(page)
    apple_pomice_page.add_apple_pomice_to_basket()
    apple_pomice_page.validate_apple_pomice()


def test_fail_on_purpose(page: Page, successful_login):
    # Click text=Monkeys love it the most.
    @allure.step
    def fail_test() -> None:
        assert page.locator(
            "text=Moose love it the most."
        ).is_visible(), "Element not visible on page"

    fail_test()
