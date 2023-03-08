from lovely.pytest.docker.compose import Services
from pytest import fixture


@fixture(scope="session", autouse=False)
def docker_juice_shop(docker_services: Services) -> None:
    test_db_service_name: str = "juice-shop"
    docker_services.start(test_db_service_name)
    docker_services.wait_for_service(test_db_service_name, 3000, timeout=60)
