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
