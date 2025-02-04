import allure
from playwright.async_api import Page


class ForgetPasswordPage:
    CHANGE: str = "#resetButton"
    EMAIL: str = "#email"
    NEW_PASSWORD: str = "#newPassword"
    NEW_PASSWORD_REPEAT: str = "#newPasswordRepeat"
    SECURITY_ANSWER: str = "#securityAnswer"

    def __init__(self, page: Page) -> None:
        self.page: Page = page

    @allure.step
    async def fill_in_data_and_confirm(self, email: str, security_answer: str, password: str) -> None:
        await self.page.locator(self.EMAIL).fill(email)
        # Click on Login
        await self.page.locator(self.SECURITY_ANSWER).fill(security_answer)
        await self.page.locator(self.NEW_PASSWORD).fill(password)
        await self.page.locator(self.NEW_PASSWORD_REPEAT).fill(password)
        # Confirm
        async with self.page.expect_navigation():
            await self.page.locator(self.CHANGE).click()
