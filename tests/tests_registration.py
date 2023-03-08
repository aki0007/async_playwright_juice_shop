from pytest import mark
from playwright.sync_api import Page

@mark.registration
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
    page.locator(
        'button[role="menuitem"]:has-text("exit_to_app Login")'
    ).click()
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
    page.locator('[aria-label="Field to confirm the password"]').fill(
        "Test123*"
    )
    # Click #registration-form div:has-text("Security Question *") >> nth=3
    page.locator('#registration-form div:has-text("Security Question *")').nth(
        3
    ).click()
    # Click text=Your eldest siblings middle name?
    page.locator("text=Your eldest siblings middle name?").click()
    # Click #registration-form div:has-text("Answer *") >> nth=3
    page.locator('#registration-form div:has-text("Answer *")').nth(3).click()
    # Fill [placeholder="Answer to your security question"]
    page.locator('[placeholder="Answer to your security question"]').fill(
        "Aki"
    )
    # Click [aria-label="Button to complete the registration"]
    # with page.expect_navigation(url="http://0.0.0.0:3000/register#/login"):
    with page.expect_navigation():
        page.locator(
            '[aria-label="Button to complete the registration"]'
        ).click()
