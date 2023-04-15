import allure
from playwright.async_api import Page

from config import conf_obj


class NavigationPage:
    OPEN_SIDENAV: str = "[aria-label='Open Sidenav']"
    SEARCH_INPUT: str = "#mat-input-0"
    SEARCH_INPUT_WRAPPER: str = "#searchQuery"

    def __init__(self, page: Page) -> None:
        self.page: Page = page

    @allure.step
    async def search(self, search_text: str) -> None:
        await self.page.locator(self.SEARCH_INPUT_WRAPPER).click()
        await self.page.locator(self.SEARCH_INPUT).fill(search_text)
        await self.page.locator(self.SEARCH_INPUT).press("Enter")

    @allure.step
    async def open_sidetab(self, tab: str) -> None:
        await self.page.locator(self.OPEN_SIDENAV).click()
        async with self.page.expect_navigation():
            await self.page.get_by_text(tab).click()

    @allure.step
    async def navigate_to_metrics(self) -> None:
        url: str = f"{conf_obj.GLOBAL_URL}/metrics".replace("#/", "")
        await self.page.goto(url)
