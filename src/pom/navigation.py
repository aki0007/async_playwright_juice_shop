import allure
from playwright.async_api import Page

from config import conf_obj


class NavigationPage:
    ACCOUNT: str = "#navbarAccount"
    NAVIGATION_LOGIN: str = "#navbarLoginButton"
    HOME_PAGE: str = "[aria-label='Back to homepage']"
    CLOSE_BUTTON: str = "button#closeButton"
    OPEN_SIDENAV: str = "[aria-label='Open Sidenav']"
    PRIVACY_AND_SECURITY: str = "button[aria-label='Show Privacy and Security Menu']"
    PRIVACY_POLICY: str = "button[aria-label='Go to privacy policy page']"
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
    async def navigate_to_metrics(self) -> None:
        await self.page.goto(f"{conf_obj.GLOBAL_URL}metrics".replace("#/", ""), wait_until="networkidle")

    @allure.step
    async def navigate_to_outdated_allowlist(self) -> None:
        redirect_url: str = "redirect?to=https://blockchain.info/address/1AbKfgvw9psQ41NbLi8kufDQTezwG8DRZm"
        await self.page.goto(f"{conf_obj.GLOBAL_URL}/{redirect_url}".replace("#/", ""), wait_until="networkidle")

    @allure.step
    async def open_side_menu_tab(self, tab: str) -> None:
        await self.page.locator(self.OPEN_SIDENAV).click()
        async with self.page.expect_navigation():
            await self.page.get_by_text(tab).click()

    @allure.step
    async def open_privacy_policy(self) -> None:
        await self.page.locator(self.ACCOUNT).click()
        await self.page.locator(self.PRIVACY_AND_SECURITY).click()
        async with self.page.expect_navigation():
            await self.page.locator(self.PRIVACY_POLICY).click()
        await self.page.wait_for_load_state("networkidle")

    @allure.step
    async def home_page(self) -> None:
        await self.page.locator(self.HOME_PAGE).click()

    @allure.step
    async def navigate_to_login(self) -> None:
        await self.page.locator(self.ACCOUNT).click()
        await self.page.locator(self.NAVIGATION_LOGIN).click()
        await self.page.wait_for_load_state("networkidle")

    @allure.step
    async def close_all_messages(self) -> None:
        elements: list = await self.page.locator(self.CLOSE_BUTTON).all()
        for close_button in elements:
            await close_button.click(modifiers=["Shift"])
