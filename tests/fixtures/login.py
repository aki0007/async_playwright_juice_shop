from pytest_asyncio import fixture
from src.pom.login import LoginPage
from config import conf_obj


@fixture(scope="function")
def successful_login(login_page: LoginPage) -> None:
    login_page.navigate_to_homepage()
    login_page.login_to_application(conf_obj.LOGIN_USERNAME, conf_obj.LOGIN_PASSWORD)
