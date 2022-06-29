import os
from datetime import datetime
from typing import Union

from dotenv import load_dotenv

load_dotenv()


class Config:
    # App
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEVICES: str = os.getenv("DEVICES", "")
    GLOBAL_URL: str = os.getenv("GLOBAL_URL", "https://")
    LOGIN_URL: str = os.getenv("LOGIN_URL", "/testing")
    LOCAL: bool = os.getenv("LOCAL", "0") == "1"
    SCREENSHOT_PATH: str = os.path.abspath(
        "reports/screenshots/" + datetime.now().strftime("%d-%m-%Y")
    )

    # Credentials
    LOGIN_USERNAME: str = os.getenv("LOGIN_USERNAME", "user")
    LOGIN_PASSWORD: str = os.getenv("LOGIN_PASSWORD", "1234")

    # Consts
    TRACE: bool = False


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
    browser_list = {
        "chrome": {"browser": "chromium"},
        "firefox": {"browser": "firefox"},
        "safari": {"browser": "webkit"},
        "edge": {"browser": "chromium", "channel": "msedge"},
    }
    env_browser: str = os.getenv("BROWSER", "chrome")
    if env_browser not in browser_list:
        raise Exception("Invalid browser")

    return browser_list[env_browser]


conf_obj: Union[Config, ProductionConfig, StagingConfig] = get_config()
