import allure
from playwright.async_api import Page


class NavigationPage:
    SEARCH_INPUT: str = "#mat-input-0"
    SEARCH_INPUT_WRAPPER: str = "#searchQuery"

    def __init__(self, page: Page) -> None:
        self.page: Page = page

    @allure.step
    async def search(self, search_text: str) -> None:
        await self.page.locator(self.SEARCH_INPUT_WRAPPER).click()
        await self.page.locator(self.SEARCH_INPUT).fill(search_text)
        await self.page.locator(self.SEARCH_INPUT).press("Enter")
