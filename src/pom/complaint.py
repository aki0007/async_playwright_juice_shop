import allure
from playwright.async_api import Page

from config import conf_obj


class ComplainPage:
    COMPLAINT_HEADER: str = "//h1[text()='Complaint']"
    COMPLAINT_FORM: str = "//div[@id='complaint-form']"
    COMPLAINER_EMAIL: str = "//span[contains(text(), '{complainer_email}}')]"
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

    @allure.step
    async def validate_email_of_complainer(self, complainer_email: str) -> None:
        await self.page.locator(self.COMPLAINER_EMAIL.format(complainer_email=complainer_email)).is_visible()
