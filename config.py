import os
from datetime import datetime
from typing import Union

from dotenv import load_dotenv

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


def get_browser() -> dict:
    env_browser: str = os.getenv("BROWSER", "chrome")
    browser_list = {
        "chrome": {"driver": "chromium"},
        "firefox": {"driver": "firefox"},
        "safari": {"driver": "webkit"},
        "edge": {"driver": "chromium", "channel": "msedge"},
    }
    if env_browser not in browser_list:
        raise Exception("Invalid browser")

    return browser_list[env_browser]


conf_obj: Union[Config, ProductionConfig, StagingConfig] = get_config()
