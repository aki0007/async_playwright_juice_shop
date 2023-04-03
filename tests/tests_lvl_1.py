from pytest import mark

from src.pom.navigation import NavigationPage
from src.pom.score_board import ScoreBoardPage


@mark.level_1
class TestLevel1:
    @staticmethod
    async def test_score_board(score_board: ScoreBoardPage) -> None:
        await score_board.navigate_to_score_board()
        # await score_board.select_star_level(1)
        await score_board.validate_completed_task("Score Board")

    @staticmethod
    async def test_dom_xss(navigation: NavigationPage, score_board: ScoreBoardPage) -> None:
        await navigation.search('<iframe src="javascript:alert(`xss`)">.')
        await score_board.navigate_to_score_board()
        await score_board.validate_completed_task("DOM XSS")
