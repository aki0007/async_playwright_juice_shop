from pytest import mark

from src.pom.login import LoginPage


@mark.registration
class TestLogin:

    @staticmethod
    async def test_register(login: LoginPage):
        await login.register()

