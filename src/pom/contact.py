import allure
from playwright.async_api import Page

from config import conf_obj


class ContactPage:
    ACCOUNT: str = "#navbarAccount"
    AUTHOR_INPUT: str = "#mat-input-1"
    AUTHOR_INPUT_DISABLED: str = "#mat-input-1:disabled"
    CAPTCHA: str = "#captcha"
    CAPTCHA_INPUT: str = "#captchaControl"
    COMMENT_TEXTAREA: str = "#comment"
    RATING_SLIDER: str = "#rating"
    RATING_SLIDER_THUMB: str = "div[class='mat-slider-thumb']"
    SUBMIT_BUTTON: str = "#submitButton"

    def __init__(self, page: Page) -> None:
        self.page: Page = page

    @allure.step
    async def solve_captcha(self) -> int:
        # pylint: disable=eval-used
        return eval(await self.page.locator(self.CAPTCHA).text_content())  # type: ignore

    @allure.step
    async def fill_inputs_and_submit(
        self, author: str = conf_obj.LOGIN_URL, comment: str = "Automated test", rating: str = "3"
    ) -> None:
        # Author
        if await self.page.locator(self.AUTHOR_INPUT_DISABLED).is_visible():
            await self.page.locator(self.AUTHOR_INPUT_DISABLED).fill(author)
        # Comment
        await self.page.locator(self.COMMENT_TEXTAREA).fill(comment)
        # Rating
        await self.page.locator(self.RATING_SLIDER).click()
        keyboard_input_num = int(rating) - 3  # Default click on Rating is 3
        if keyboard_input_num > 0:  # Rating 3 and 4
            for _ in range(keyboard_input_num):
                await self.page.keyboard.press("ArrowRight")
        elif keyboard_input_num < 0:  # Rating 1 and 2
            for _ in range(abs(keyboard_input_num)):
                await self.page.keyboard.press("ArrowLeft")
        # Captcha
        captcha: int = await self.solve_captcha()
        await self.page.locator(self.CAPTCHA_INPUT).fill(str(captcha))
        await self.page.pause()
        # Submit
        await self.page.locator(self.SUBMIT_BUTTON).click()
