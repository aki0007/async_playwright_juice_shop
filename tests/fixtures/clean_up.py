import os
from typing import AsyncGenerator

from pytest_asyncio import fixture

from constants import SessionConstants


@fixture(scope="session", autouse=True)
async def clean_up_files() -> AsyncGenerator[None, None, None]:
    yield
    for file in SessionConstants.FILES_TO_DELETE:
        if not os.path.exists(file):
            continue
        os.remove(file)
