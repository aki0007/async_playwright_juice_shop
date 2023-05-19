import allure
from playwright.async_api import Page

from config import conf_obj


class ComplainPage:
    CHOOSE_FILE_INPUT: str = "#file"
    MESSAGE_TEXTAREA: str = "#complaintMessage"
    SUBMIT_BUTTON: str = "#submitButton"

    def __init__(self, page: Page) -> None:
        self.page: Page = page

    @allure.step
    async def navigate_to_complain(self) -> None:
        await self.page.goto(f"{conf_obj.GLOBAL_URL}/complain", wait_until="networkidle")

    @allure.step
    async def upload_invoice(self, message: str, file: str) -> None:
        await self.page.locator(self.MESSAGE_TEXTAREA).fill(message)
        await self.page.locator(self.CHOOSE_FILE_INPUT).set_input_files(file)
        await self.page.locator(self.SUBMIT_BUTTON).click()
