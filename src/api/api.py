from typing import Any

import allure
from playwright.async_api import APIRequestContext
from playwright.async_api._generated import APIResponse

from config import conf_obj


class AsyncAPI:
    def __init__(self, api_request_context: APIRequestContext) -> None:
        self.api: APIRequestContext = api_request_context

    @allure.step
    async def async_get(self, url: str) -> APIResponse:
        url = (conf_obj.GLOBAL_URL + url).replace("#", "")
        response: APIResponse = await self.api.get(url)
        return response

    @allure.step
    async def async_post(self, url: str, data: Any = None) -> APIResponse:
        url = (conf_obj.GLOBAL_URL + url).replace("#", "")
        response: APIResponse = await self.api.post(url=url, data=data)
        return response

    @allure.step
    async def async_login(self, data: Any = None) -> APIResponse:
        return await self.async_post("rest/user/login", data)
