from pytest import mark

from src.pom.api import AsyncAPI
from src.pom.chat_bot import ChatBotPage
from src.pom.navigation import NavigationPage
from src.pom.photo_wall import PhotoWallPage
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
        await score_board.validate_completed_task("DOM XSS")

    @staticmethod
    async def test_bonus_payload(navigation: NavigationPage, score_board: ScoreBoardPage) -> None:
        bonus_payload = """
        <iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/771984076&color=%23ff5500&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe>
        """
        await navigation.search(bonus_payload)
        await score_board.validate_completed_task("Bonus Payload")

    @staticmethod
    async def test_bully_chatbot(navigation: NavigationPage, chatbot: ChatBotPage, score_board: ScoreBoardPage) -> None:
        await navigation.open_sidetab("Support Chat")
        await chatbot.annoy_chatbot_with_word("discount")
        await score_board.validate_completed_task("Bully Chatbot")

    @staticmethod
    async def test_confidential_document(async_api: AsyncAPI, score_board: ScoreBoardPage) -> None:
        await async_api.async_get("ftp/acquisitions.md")
        await score_board.validate_completed_task("Confidential Document")

    @staticmethod
    async def test_error_handling(async_api: AsyncAPI, score_board: ScoreBoardPage) -> None:
        await async_api.async_get("error-test")
        await score_board.validate_completed_task("Error Handling")

    @staticmethod
    async def test_exposed_metrics(navigation: NavigationPage, score_board: ScoreBoardPage) -> None:
        await navigation.navigate_to_metrics()
        await score_board.validate_completed_task("Exposed Metrics")

    @staticmethod
    async def test_missing_encoding(navigation: NavigationPage, photo_wall: PhotoWallPage, score_board: ScoreBoardPage) -> None:
        await navigation.open_sidetab("Photo Wall")
        await photo_wall.fix_broken_image()
        await score_board.validate_completed_task("Missing Encoding")

    @staticmethod
    async def test_outdated_allowlist(navigation: NavigationPage, photo_wall: PhotoWallPage, score_board: ScoreBoardPage) -> None:
        await navigation.navigate_to_outdated_allowlist()
        await score_board.validate_completed_task("Outdated Allowlist")
