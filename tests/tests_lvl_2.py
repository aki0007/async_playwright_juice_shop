from pytest import mark

from constants import SessionConstants
from src.api.api import AsyncAPI
from src.api.interceptor import AsyncInterceptor
from src.pom.administration import AdministrationPage
from src.pom.complain import ComplainPage
from src.pom.login import LoginPage
from src.pom.navigation import NavigationPage
from src.pom.score_board import ScoreBoardPage


@mark.level_2
class TestLevel2:
    @staticmethod
    async def test_login_admin(
        login: LoginPage, async_interceptor: AsyncInterceptor, navigation: NavigationPage, score_board: ScoreBoardPage
    ) -> None:
        await login.logout()
        await navigation.navigate_to_login()
        await async_interceptor.login_sql_injection()
        await login.login_to_app(username="admin", password="admin")
        await score_board.validate_completed_task("Login Admin", star=2)

    @staticmethod
    async def test_password_strength(
        async_interceptor: AsyncInterceptor, async_api: AsyncAPI, score_board: ScoreBoardPage
    ) -> None:
        await async_interceptor.brute_force_login(username="admin@juice-sh.op", async_api=async_api)
        await score_board.validate_completed_task("Password Strength", star=2)

    @staticmethod
    async def test_admin_section(
        administration: AdministrationPage, login: LoginPage, navigation: NavigationPage, score_board: ScoreBoardPage
    ) -> None:
        await login.logout()
        await navigation.navigate_to_login()
        await login.login_to_app(username="admin@juice-sh.op", password="admin123")  # Password found in previous test
        await administration.navigate_to_administration()
        await score_board.validate_completed_task("Admin Section", star=2)

    @staticmethod
    async def test_deprecated_interface(navigation: NavigationPage, complain: ComplainPage, score_board: ScoreBoardPage) -> None:
        await navigation.open_side_menu_tab("Complaint")
        await complain.upload_invoice(message="test", file=SessionConstants.DEPRECATED_INTERFACE)
        await score_board.validate_completed_task("Deprecated Interface", star=2)

    @staticmethod
    async def test_five_star_feedback(
        navigation: NavigationPage, login: LoginPage, administration: AdministrationPage, score_board: ScoreBoardPage
    ) -> None:
        await login.logout()
        await navigation.navigate_to_login()
        await login.login_to_app(username="admin@juice-sh.op", password="admin123")  # Password found in previous test
        await administration.navigate_to_administration()
        await administration.delete_file_star_comment()
        await score_board.validate_completed_task("Admin Section", star=2)

    @staticmethod
    async def test_login_mc_safe_search(
        navigation: NavigationPage, login: LoginPage, administration: AdministrationPage, score_board: ScoreBoardPage
    ) -> None:
        await login.logout()
        await navigation.navigate_to_login()
        await login.login_to_app(username="mc.safesearch@juice-sh.op", password="Mr. N00dles")
        await score_board.validate_completed_task("Login MC SafeSearch", star=2)
