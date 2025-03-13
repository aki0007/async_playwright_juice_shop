import allure
from playwright.async_api import Page

from config import conf_obj
from general.assertion import AssertionMethod


class ScoreBoardPage:
    STAR_LEVEL: str = "#mat-button-toggle-{level}-button"
    STAR_LEVEL_CLICKED: str = STAR_LEVEL + "[aria-pressed='true']"
    SOLVED_ROW: str = "mat-cell:has-text('{task}')+mat-cell>app-challenge-status-badge"
    SOLVED_ROWS_TABLE: str = "mat-row[role='row']"
    SOLVED_ROW_XPATH: str = ".solved.ng-star-inserted .name:has-text('{task}')"
    SOLVED_CHALANGE: str = ".solved.ng-star-inserted .name:has-text('{task}')"

    def __init__(self, page: Page) -> None:
        self.page: Page = page

    @allure.step
    async def navigate_to_score_board(self) -> None:
        await self.page.goto(f"{conf_obj.GLOBAL_URL}/score-board", wait_until="networkidle")

    @allure.step
    async def select_star_level(self, level: int) -> None:
        if self.page.locator(self.STAR_LEVEL_CLICKED.format(level=level)):
            return
        await self.page.locator(self.STAR_LEVEL.format(level=level)).click()

    @allure.step
    async def click_on_johns_forget_password(self) -> None:
        async with self.page.expect_navigation():
            await self.page.get_by_text("Forgot Password").first.click()

    @allure.step
    async def validate_completed_task(self, task: str, star: int = 1, retry: int = 0) -> None:
        try:
            if "score-board" not in self.page.url:
                await self.navigate_to_score_board()
            # If necessary select star level
            await self.select_star_level(star)

            await AssertionMethod.wait_for_selector_to_become_visible(self.page, self.SOLVED_CHALANGE.format(task=task), 1)
        # Retry:
        except AssertionError:
            if retry < 2:
                await self.page.reload(wait_until="networkidle")
                await self.validate_completed_task(task, star, retry + 1)

            else:
                await AssertionMethod.wait_for_selector_to_become_visible(self.page, self.SOLVED_ROW_XPATH.format(task=task), 1)
