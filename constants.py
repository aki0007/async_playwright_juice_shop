from datetime import datetime

CURRENT_DATE: str = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")


class SessionConstants:
    # Report path created in test run
    ALLURE_HISTORY_PATH: str = "report/allure-history/" + CURRENT_DATE
    ALLURE_REPORT_PATH: str = "report/allure-report/"
    RESOURCES_PATH: str = "tests/test_resources/"
    SCREENSHOT_PATH: str = "report/screenshots/" + CURRENT_DATE
    STORAGE_STATE: str = "state.json"

    # Cookies
    COOKIES: list = []

    # Variables used for tracing
    DEFAULT_TIMEOUT: int = 60 * 1000  # in seconds
    TEST_NAME: str = ""
    TRACE: bool = False
