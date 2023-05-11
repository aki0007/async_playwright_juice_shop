import allure
from playwright.async_api import Page

from config import conf_obj


class AdministrationPage:
    FIVE_STAR_COMMENT_DELETE_BUTTON: str = "mat-row:has(mat-icon:nth-child(5)) button"

    def __init__(self, page: Page) -> None:
        self.page: Page = page

    @allure.step
    async def navigate_to_administration(self) -> None:
        await self.page.goto(f"{conf_obj.GLOBAL_URL}/administration", wait_until="networkidle")

    @allure.step
    async def delete_file_star_comment(self) -> None:
        # In case test is already run first check if 5-star comment exists:
        if await self.page.locator(self.FIVE_STAR_COMMENT_DELETE_BUTTON).is_visible():
            await self.page.locator(self.FIVE_STAR_COMMENT_DELETE_BUTTON).click()
