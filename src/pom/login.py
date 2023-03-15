import allure
from playwright.async_api import Page

from config import conf_obj


class LoginPage:
    CLOSE_WELCOME_BANNER: str = "[aria-label='Close Welcome Banner']"
    DISMISS_BUTTON: str = "[aria-label='dismiss cookie message']"
    EMAIL_MUST_BE_UNIQUE: str = ".error"
    GO_TO_LOGIN_PAGE: str = "#navbarLoginButton"
    LOGIN_BUTTON: str = "button[id='loginButton']"
    LOGIN_EMAIL_INPUT: str = "#email"
    LOGIN_PASSWORD_INPUT: str = "#password"
    NAV_BAR: str = "#navbarAccount"
    NEW_CUSTOMER: str = "#newCustomerLink"
    REGISTER_EMAIL_INPUT: str = "#emailControl"
    REGISTER_PASSWORD_INPUT: str = "#passwordControl"
    REPEAT_REGISTER_PASSWORD_INPUT: str = "#repeatPasswordControl"
    SECURITY_QUESTION: str = "div[id^='mat-select-value']"
    SECURITY_QUESTION_ANSWER: str = "#securityAnswerControl"
    SECURITY_QUESTION_SPAN: str = "span:has-text('{question}')"
    SUCCESSFUL_REGISTRATION: str = (
        "span:has-text('Registration completed successfully. You can now log in.')"
    )
    REGISTER_BUTTON: str = "#registerButton"
    WELCOME_BANNER: str = "#cdk-overlay-1"

    def __init__(self, page: Page) -> None:
        self.page: Page = page

    @allure.step
    async def navigate_to_homepage(self) -> None:
        # Go to https://juice-shop.herokuapp.com/login
        await self.page.goto(conf_obj.GLOBAL_URL + conf_obj.LOGIN_URL)
        # Close welcome banner
        if await self.page.locator(self.WELCOME_BANNER).is_visible():
            await self.page.locator(self.CLOSE_WELCOME_BANNER).click()
        # Close cookie banner
        if await self.page.locator(self.DISMISS_BUTTON).is_visible():
            await self.page.locator(self.DISMISS_BUTTON).click()

    @allure.step
    async def login_to_app(self, username, password) -> None:
        await self.page.locator(self.NAV_BAR).click()
        # Click on Login
        await self.page.locator(self.GO_TO_LOGIN_PAGE).click()
        await self.page.wait_for_url("**/login")
        # Set up User registration data
        await self.page.locator(self.LOGIN_EMAIL_INPUT).fill(username)
        await self.page.locator(self.LOGIN_PASSWORD_INPUT).fill(password)
        # Click Log in
        await self.page.locator(self.LOGIN_BUTTON).click()

    @allure.step
    async def register(self, username, password, security_answer) -> None:
        await self.page.locator(self.NAV_BAR).click()
        # Click on Login
        await self.page.locator(self.GO_TO_LOGIN_PAGE).click()
        await self.page.wait_for_url("**/login")
        # Click on "Not yet a customer"
        await self.page.locator(self.NEW_CUSTOMER).click()
        await self.page.wait_for_url("**/register")

        # Set up User registration data
        await self.page.locator(self.REGISTER_EMAIL_INPUT).fill(username)
        await self.page.locator(self.REGISTER_PASSWORD_INPUT).fill(password)
        await self.page.locator(self.REPEAT_REGISTER_PASSWORD_INPUT).fill(password)
        # Choose security question
        await self.page.locator(self.SECURITY_QUESTION).click()
        await self.page.locator(
            self.SECURITY_QUESTION_SPAN.format(
                question="Your eldest siblings middle name?"
            )
        ).click()
        await self.page.locator(self.SECURITY_QUESTION_ANSWER).fill(security_answer)
        # Click Register
        await self.page.locator(self.REGISTER_BUTTON).click()

        # Log in
        await self.login_to_app(username, password)
