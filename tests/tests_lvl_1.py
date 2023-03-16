from pytest import mark

from src.pom.score_board import ScoreBoardPage


@mark.level_1
class TestLevel1:
    @staticmethod
    async def test_score_board(score_board: ScoreBoardPage):
        await score_board.navigate_to_score_board()
        await score_board.validate_completed_task("Score Board")
