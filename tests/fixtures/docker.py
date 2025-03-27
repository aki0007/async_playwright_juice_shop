import os

from lovely.pytest.docker.compose import Services
from pytest import Config
from pytest_asyncio import fixture

import config


@fixture(scope="session")
async def docker_services_project_name(pytestconfig: Config) -> str:
    return "juice-shop"


@fixture(scope="session")
def docker_compose_files(pytestconfig: Config) -> list:
    return [os.path.join(str(pytestconfig.rootpath), "docker-compose.yml")]


@fixture(scope="session", autouse=config.LOCAL != 1)
async def docker_juice_shop(docker_services: Services) -> None:
    docker_service_name: str = "juice_shop"
    docker_services.start(docker_service_name)
    docker_services.wait_for_service(docker_service_name, 3000, timeout=5)
