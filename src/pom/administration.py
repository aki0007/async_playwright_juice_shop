import allure
from playwright.async_api import Page

from config import conf_obj


class AdministrationPage:
    def __init__(self, page: Page) -> None:
        self.page: Page = page

    @allure.step
    async def navigate_to_administration(self) -> None:
        await self.page.goto(f"{conf_obj.GLOBAL_URL}/administration")
