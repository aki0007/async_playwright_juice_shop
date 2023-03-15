from pytest import mark

from src.pom.login import LoginPage


@mark.registration
class TestLogin:
    @staticmethod
    async def test_1(login: LoginPage):
        pass
