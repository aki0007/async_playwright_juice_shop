from pytest import mark

from src.api.api import AsyncAPI
from src.api.interceptor import AsyncInterceptor
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
        login: LoginPage, async_interceptor: AsyncInterceptor, async_api: AsyncAPI, score_board: ScoreBoardPage
    ) -> None:
        await async_interceptor.brute_force_login(username="admin@juice-sh.op", async_api=async_api)
        await score_board.validate_completed_task("Password Strength", star=2)
