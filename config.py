import os
from datetime import datetime
from typing import Union

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Browser, Playwright

load_dotenv()


class Config:
    # App
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    GLOBAL_URL = os.getenv("GLOBAL_URL", "https://")
    LOGIN_URL = os.getenv("LOGIN_URL", "/testing")
    LOCAL: bool = os.getenv("LOCAL", "0") == "1"
    SCREENSHOT_PATH = os.path.abspath(
        "reports/screenshots/" + datetime.now().strftime("%d-%m-%Y")
    )

    # Credentials
    LOGIN_USERNAME = os.getenv("LOGIN_USERNAME", "user")
    LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD", "1234")


class ProductionConfig(Config):
    ENVIRONMENT: str = "production"


class StagingConfig(Config):
    ENVIRONMENT: str = "staging"


def get_config() -> Union[Config, ProductionConfig, StagingConfig]:
    env_list: dict = {
        "development": Config,
        "docker": Config,
        "production": ProductionConfig,
        "staging": StagingConfig,
    }
    env: str = os.getenv("ENVIRONMENT", "development")

    if env not in env_list:
        raise Exception("Invalid environment")

    return env_list[env]()


def get_browser() -> Browser:
    browser: Playwright = sync_playwright().start()
    env_browser: str = os.getenv("BROWSER", "chrome")

    browser_list = {
             "chrome": browser.chromium.launch(headless=False) if conf_obj.LOCAL else browser.chromium.launch(),
             "firefox": browser.firefox.launch(headless=False) if conf_obj.LOCAL else browser.firefox.launch(),
             "safari": Exception("Invalid browser") if conf_obj.LOCAL else browser.webkit.launch(),
             # "edge": browser.chromium.launch(headless=False, channel="msedge") if conf_obj.LOCAL
             # else browser.chromium.launch(channel="msedge")
    }
    if env_browser not in browser_list:
        raise Exception("Invalid browser")

    return browser_list[env_browser]


conf_obj: Union[Config, ProductionConfig, StagingConfig] = get_config()
