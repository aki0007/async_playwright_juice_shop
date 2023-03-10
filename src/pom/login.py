import allure
from playwright.async_api import Page

from config import conf_obj


class LoginPage:
    EMAIL_INPUT: str = '[aria-label="Text\\ field\\ for\\ the\\ login\\ email"]'
    HAS_TEXT_EMAIL: str = '#login-form div:has-text("Email *")'
    HAS_TEXT_PASSWORD: str = (
        '[aria-label="Text\\ field\\ for\\ the\\ login\\ password"]'
    )
    LOGIN_BUTTON: str = '[aria-label="Login"]'
    LOGIN_MENU_ITEM: str = 'button[role="menuitem"]:has-text("exit_to_app Login")'
    PASSWORD_INPUT: str = '[aria-label="Text\\ field\\ for\\ the\\ login\\ password"]'
    SHOW_ACCOUNT_MENU: str = '[aria-label="Show\\/hide\\ account\\ menu"]'
    WELCOME_BANNER: str = '[aria-label="Close\\ Welcome\\ Banner"]'
    COOKIE_BANNER: str = "text=Me want it!"

    def __init__(self, page: Page) -> None:
        self.page: Page = page

    @allure.step
    async def navigate_to_homepage(self) -> None:
        # Go to https://juice-shop.herokuapp.com/login
        await self.page.goto(conf_obj.GLOBAL_URL + conf_obj.LOGIN_URL)
        # Click [aria-label="Close\ Welcome\ Banner"]
        if self.page.locator(self.COOKIE_BANNER).is_visible():
            await self.page.locator(self.COOKIE_BANNER).click()

        if self.page.locator(self.WELCOME_BANNER).is_visible():
            await self.page.locator(self.WELCOME_BANNER).click()

    @allure.step
    async def login_to_application(self, username, password) -> None:
        # Click [aria-label="Show\/hide\ account\ menu"]
        await self.page.locator(self.SHOW_ACCOUNT_MENU).click()
        # Click button[role="menuitem"]:has-text("exit_to_app Login")
        await self.page.locator(self.LOGIN_MENU_ITEM).click()
        assert (
            self.page.url
            == conf_obj.GLOBAL_URL + "/login#" + conf_obj.LOGIN_URL
        )
        # Click #login-form div:has-text("Email *") >> nth=2
        await self.page.locator(self.HAS_TEXT_EMAIL).nth(2).click()
        # Fill [aria-label="Text\ field\ for\ the\ login\ email"]
        await self.page.locator(self.EMAIL_INPUT).fill(username)
        # Click [aria-label="Text\ field\ for\ the\ login\ password"]
        await self.page.locator(self.HAS_TEXT_PASSWORD).click()
        # Fill [aria-label="Text\ field\ for\ the\ login\ password"]
        await self.page.locator(self.PASSWORD_INPUT).fill(password)
        # Click [aria-label="Login"]
        await self.page.locator(self.LOGIN_BUTTON).click()

    @allure.step
    async def register(self) -> None:
        # Leave the test like this to show how codegen creates code
        # Go to http://0.0.0.0:3000/register
        await self.page.goto("http://0.0.0.0:3000/register")
        # Click [aria-label="Close Welcome Banner"]
        await self.page.locator('[aria-label="Close Welcome Banner"]').click()
        # Click [aria-label="Show\/hide account menu"]
        await self.page.locator('[aria-label="Show\\/hide account menu"]').click()
        # Click button[role="menuitem"]:has-text("exit_to_app Login")
        await self.page.locator(
            'button[role="menuitem"]:has-text("exit_to_app Login")'
        ).click()
        # expect(page).to_have_url("http://0.0.0.0:3000/register#/login")
        # Click text=Not yet a customer?
        await self.page.locator("text=Not yet a customer?").click()
        # expect(page).to_have_url("http://0.0.0.0:3000/register#/register")
        # Click [aria-label="Email address field"]
        await self.page.locator('[aria-label="Email address field"]').click()
        # Fill [aria-label="Email address field"]
        await self.page.locator('[aria-label="Email address field"]').fill(
            "jaksa.milanovic007@gmail.com"
        )
        # Click [aria-label="Field for the password"]
        await self.page.locator('[aria-label="Field for the password"]').click()
        # Fill [aria-label="Field for the password"]
        await self.page.locator('[aria-label="Field for the password"]').fill("Test123*")
        # Click [aria-label="Field to confirm the password"]
        await self.page.locator('[aria-label="Field to confirm the password"]').click()
        # Fill [aria-label="Field to confirm the password"]
        await self.page.locator('[aria-label="Field to confirm the password"]').fill(
            "Test123*"
        )
        # Click #registration-form div:has-text("Security Question *") >> nth=3
        await self.page.locator('#registration-form div:has-text("Security Question *")').nth(
            3
        ).click()
        # Click text=Your eldest siblings middle name?
        await self.page.locator("text=Your eldest siblings middle name?").click()
        # Click #registration-form div:has-text("Answer *") >> nth=3
        await self.page.locator('#registration-form div:has-text("Answer *")').nth(3).click()
        # Fill [placeholder="Answer to your security question"]
        await self.page.locator('[placeholder="Answer to your security question"]').fill(
            "Aki"
        )
