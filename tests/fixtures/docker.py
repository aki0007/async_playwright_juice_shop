import time

from lovely.pytest.docker.compose import Services
from pytest_asyncio import fixture


@fixture(scope="session", autouse=True)
async def docker_juice_shop(docker_services: Services) -> None:
    test_db_service_name: str = "juice-shop"
    docker_services.start(test_db_service_name)
    time.sleep(2)
