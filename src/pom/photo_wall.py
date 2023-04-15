import urllib.parse
from typing import Optional

import allure
from playwright.async_api import Page


class PhotoWallPage:
    BROKEN_IMAGE: str = "[alt='😼 #zatschi #whoneedsfourlegs']"
    JS_SET_ATTRIBUTE_COMMAND: str = 'document.querySelector("{element}").setAttribute("{attribute}", "{value}");'

    def __init__(self, page: Page) -> None:
        self.page: Page = page

    @allure.step
    async def fix_broken_image(self) -> None:
        # Get broken img src
        decoded_src: str = urllib.parse.quote(await self.page.locator(self.BROKEN_IMAGE).get_attribute("src"))
        await self.page.evaluate(
            self.JS_SET_ATTRIBUTE_COMMAND.format(element=self.BROKEN_IMAGE, attribute="src", value=decoded_src)
        )
