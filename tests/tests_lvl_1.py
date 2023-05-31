from pytest import mark

from src.api.api import AsyncAPI
from src.api.interceptor import AsyncInterceptor
from src.pom.chat_bot import ChatBotPage
from src.pom.contact import ContactPage
from src.pom.login import LoginPage
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
        await navigation.open_side_menu_tab("Support Chat")
        await chatbot.annoy_chatbot_with_word("discount")
        await score_board.validate_completed_task("Bully Chatbot")

    @staticmethod
    async def test_confidential_document(async_api: AsyncAPI, score_board: ScoreBoardPage) -> None:
        await async_api.async_get("ftp/acquisitions.md")
        await score_board.validate_completed_task("Confidential Document")

    @staticmethod
    async def test_error_handling(async_api: AsyncAPI, score_board: ScoreBoardPage) -> None:
        await async_api.async_get("rest/4ry007")
        await score_board.validate_completed_task("Error Handling")

    @staticmethod
    async def test_exposed_metrics(navigation: NavigationPage, score_board: ScoreBoardPage) -> None:
        await navigation.navigate_to_metrics()
        await score_board.validate_completed_task("Exposed Metrics")

    @staticmethod
    async def test_missing_encoding(navigation: NavigationPage, photo_wall: PhotoWallPage, score_board: ScoreBoardPage) -> None:
        await navigation.open_side_menu_tab("Photo Wall")
        await photo_wall.fix_broken_image()
        await score_board.validate_completed_task("Missing Encoding")

    @staticmethod
    async def test_outdated_allowlist(navigation: NavigationPage, score_board: ScoreBoardPage) -> None:
        await navigation.navigate_to_outdated_allowlist()
        await score_board.validate_completed_task("Outdated Allowlist")

    @staticmethod
    async def test_privacy_policy(navigation: NavigationPage, score_board: ScoreBoardPage) -> None:
        await navigation.open_privacy_policy()
        await score_board.validate_completed_task("Privacy Policy")

    @staticmethod
    async def test_zero_feedback(
        navigation: NavigationPage, async_interceptor: AsyncInterceptor, contact: ContactPage, score_board: ScoreBoardPage
    ) -> None:
        mock_data = {"rating": 0}
        await navigation.open_side_menu_tab("Customer Feedback")
        await async_interceptor.mock_feedback_request("**/api/Feedbacks/", mock_data)
        await contact.fill_inputs_and_submit()
        await score_board.validate_completed_task("Zero Stars")

    @staticmethod
    async def test_repetitive_registration(login: LoginPage, score_board: ScoreBoardPage) -> None:
        await login.logout()
        await login.not_yet_a_customer()
        await login.repetitive_registration()
        await score_board.validate_completed_task("Repetitive Registration")

    # @staticmethod
    # async def test_mass_dispel(navigation: NavigationPage, score_board: ScoreBoardPage) -> None:
    #    await navigation.home_page()
    #    await navigation.close_all_messages()
    #    await score_board.validate_completed_task("Mass Dispel")
