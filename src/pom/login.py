import allure
from playwright.async_api import Page

from config import conf_obj
from constants import CURRENT_DATE
from general.assertion import AssertionMethod


class LoginPage:
    CLOSE_WELCOME_BANNER: str = "[aria-label='Close Welcome Banner']"
    CLOSE_SUCCESSFUL_REGISTRATION_MESSAGE: str = "[class='mat-focus-indicator mat-button mat-button-base']"
    DISMISS_BUTTON: str = "[aria-label='dismiss cookie message']"
    EMAIL_MUST_BE_UNIQUE: str = "Email must be unique"
    GO_TO_LOGIN_PAGE: str = "#navbarLoginButton"
    LOGIN_BUTTON: str = "button[id='loginButton']"
    LOGIN_EMAIL_INPUT: str = "#email"
    LOGIN_PASSWORD_INPUT: str = "#password"
    LOGOUT: str = "#navbarLogoutButton"
    NAV_BAR: str = "#navbarAccount"
    NEW_CUSTOMER: str = "#newCustomerLink"
    REGISTER_EMAIL_INPUT: str = "#emailControl"
    REGISTER_PASSWORD_INPUT: str = "#passwordControl"
    REPEAT_REGISTER_PASSWORD_INPUT: str = "#repeatPasswordControl"
    SECURITY_QUESTION: str = "//mat-label[contains(text(), 'Security Question')]"
    SECURITY_QUESTION_ANSWER: str = "#securityAnswerControl"
    SECURITY_QUESTION_SPAN: str = "span:has-text('{question}')"
    SUCCESSFUL_REGISTRATION_MESSAGE: str = "span:has-text('Registration completed successfully. You can now log in.')"
    REGISTER_BUTTON: str = "#registerButton"
    WELCOME_BANNER: str = "#cdk-overlay-1"

    def __init__(self, page: Page) -> None:
        self.page: Page = page

    @allure.step
    async def navigate_to_homepage(self) -> None:
        # Go to https://juice-shop.herokuapp.com/login
        await self.page.goto(conf_obj.GLOBAL_URL + conf_obj.LOGIN_URL)
        # Close cookie banner
        if await self.page.locator(self.DISMISS_BUTTON).is_visible():
            await self.page.locator(self.DISMISS_BUTTON).click()
        # Close welcome banner
        if await self.page.locator(self.WELCOME_BANNER).is_visible():
            await self.page.locator(self.CLOSE_WELCOME_BANNER).click()

    @allure.step
    async def login_from_registration(self, username: str, password: str) -> None:
        await self.page.locator(self.NAV_BAR).click()
        # Click on Login
        await self.page.locator(self.GO_TO_LOGIN_PAGE).click()
        await self.page.wait_for_url("**/login")
        await self.login_to_app(username=username, password=password)

    @allure.step
    async def login_to_app(self, username: str, password: str) -> None:
        # Set up User registration data
        await self.page.locator(self.LOGIN_EMAIL_INPUT).fill(username)
        await self.page.locator(self.LOGIN_PASSWORD_INPUT).fill(password)
        # Click Log in
        async with self.page.expect_navigation():
            await self.page.locator(self.LOGIN_BUTTON).click()

    @allure.step
    async def register(self, username: str, password: str, security_answer: str) -> None:
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
        await self.page.pause()
        await self.page.locator(self.SECURITY_QUESTION).click()
        await self.page.locator(self.SECURITY_QUESTION_SPAN.format(question="Your eldest siblings middle name?")).click()
        await self.page.locator(self.SECURITY_QUESTION_ANSWER).fill(security_answer)
        # Click Register
        await self.page.locator(self.REGISTER_BUTTON).click()

    async def validate_successful_registration(self) -> None:
        try:
            # Validate successful login message and close it
            await AssertionMethod.wait_for_selector_to_become_visible(self.page, self.SUCCESSFUL_REGISTRATION_MESSAGE, 3)
            await self.page.get_by_role("button", name="X").click()

        except:
            print("Email must be unique")
            # await expect(self.page.get_by_text(self.EMAIL_MUST_BE_UNIQUE)).to_be_visible(timeout=3)

    async def logout(self) -> None:
        await self.page.locator(self.NAV_BAR).click()
        await self.page.locator(self.LOGOUT).click()
        await self.page.wait_for_load_state("networkidle")

    async def not_yet_a_customer(self) -> None:
        await self.page.locator(self.NAV_BAR).click()
        await self.page.locator(self.GO_TO_LOGIN_PAGE).click()
        await self.page.wait_for_url("**/login")
        await self.page.get_by_text("Not yet a customer?").click()
        await self.page.wait_for_url("**/register")

    async def repetitive_registration(self, username: str = f"temp+{CURRENT_DATE}@gmail.com", password: str = "temp123") -> None:
        await self.page.locator(self.REGISTER_EMAIL_INPUT).fill(username)
        await self.page.locator(self.REGISTER_PASSWORD_INPUT).fill(password)
        await self.page.locator(self.REPEAT_REGISTER_PASSWORD_INPUT).fill(password)
        # Choose security question
        await self.page.locator(self.SECURITY_QUESTION).click()
        await self.page.locator(self.SECURITY_QUESTION_SPAN.format(question="Your eldest siblings middle name?")).click()
        await self.page.locator(self.SECURITY_QUESTION_ANSWER).fill("Aki")
        await self.page.locator(self.REGISTER_PASSWORD_INPUT).fill(password + "456")

        # Click Register
        await self.page.locator(self.REGISTER_BUTTON).click()
