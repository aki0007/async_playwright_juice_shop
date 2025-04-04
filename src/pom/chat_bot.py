import allure
from playwright.async_api import Page

from config import conf_obj


class ChatBotPage:
    COUPON_MESSAGE: str = "//div[contains(text(), '10% coupon code for you:')]"
    INIT_MESSAGE: str = "#message-input"
    NOTIFICATION_MESSAGE: str = ".notificationMessage"
    CLOSE_NOTIFICATION_MESSAGE_BUTTON: str = "//div[@class='notificationMessage']//button[@id='closeButton']"
    CLOSE_MAT_CARD_BUTTON: str = "//mat-card[@appearance='outlined']//button[@id='closeButton']"

    def __init__(self, page: Page) -> None:
        self.page: Page = page

    @allure.step
    async def navigate_to_chat_bot(self) -> None:
        await self.page.goto(f"{conf_obj.GLOBAL_URL}/chatbot", wait_until="networkidle")

    @allure.step
    async def annoy_chatbot_with_word(self, word: str, retry: int = 0) -> None:
        while not (retry < 30 and await self.check_chat_bot_answer):
            await self.page.locator(self.INIT_MESSAGE).fill(word, timeout=500)
            await self.page.locator(self.INIT_MESSAGE).press("Enter")

            retry = retry + 1

    @allure.step
    async def check_chat_bot_answer(self, word: str) -> bool:
        return await self.page.locator(self.COUPON_MESSAGE).is_visible() == word

    @allure.step
    async def close_notification_bar_message_button(self) -> None:
        if await self.page.locator(self.CLOSE_NOTIFICATION_MESSAGE_BUTTON).is_visible():
            await self.page.locator(self.CLOSE_NOTIFICATION_MESSAGE_BUTTON).click()

    @allure.step
    async def close_mat_card_button(self) -> None:
        if await self.page.locator(self.CLOSE_MAT_CARD_BUTTON).is_visible():
            await self.page.locator(self.CLOSE_MAT_CARD_BUTTON).click()

    @allure.step
    async def close_all_pop_ups(self) -> None:
        await self.close_mat_card_button()
        await self.close_notification_bar_message_button()
