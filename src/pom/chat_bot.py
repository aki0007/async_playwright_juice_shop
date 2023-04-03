import allure
from playwright.async_api import Page

from config import conf_obj


class ChatBotPage:
    COUPON_MESSAGE: str = "//div[contains(text(), '10% coupon code for you:')]"
    INIT_MESSAGE: str = "#message-input"

    def __init__(self, page: Page) -> None:
        self.page: Page = page

    @allure.step
    async def navigate_to_chat_bot(self) -> None:
        await self.page.goto(f"{conf_obj.GLOBAL_URL}/chatbot")

    @allure.step
    async def annoy_chatbot_with_word(self, word: str, retry: int = 0) -> None:
        while not (retry < 30 and await self.page.locator(self.COUPON_MESSAGE).is_visible()):
            await self.page.locator(self.INIT_MESSAGE).fill(word, timeout=500)
            await self.page.locator(self.INIT_MESSAGE).press("Enter")

            retry = retry + 1
