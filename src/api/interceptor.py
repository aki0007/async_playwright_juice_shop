import allure
from playwright.async_api import Page
from playwright.async_api._generated import Request, Route


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
