import allure
from playwright.async_api import Page

from config import conf_obj
from general.assertion import AssertionMethod


class ScoreBoardPage:
    STAR_LEVEL: str = "#mat-button-toggle-{level}-button"
    SOLVED_ROW: str = "mat-cell:has-text('{task}')+mat-cell>app-challenge-status-badge"
    SOLVED_ROWS_TABLE: str = "mat-row[role='row']"
    SOLVED_ROW_XPATH: str = '[id="{task}.solved"]'

    def __init__(self, page: Page) -> None:
        self.page: Page = page

    @allure.step
    async def navigate_to_score_board(self) -> None:
        await self.page.goto(f"{conf_obj.GLOBAL_URL}/score-board")

    @allure.step
    async def select_star_level(self, level: int) -> None:
        await self.page.pause()
        await self.page.locator(self.STAR_LEVEL.format(level=level)).click()

    @allure.step
    async def validate_completed_task(self, task: str) -> None:
        await AssertionMethod.wait_for_selector_to_become_visible(self.page, self.SOLVED_ROW_XPATH.format(task=task))

        await self.page.pause()
