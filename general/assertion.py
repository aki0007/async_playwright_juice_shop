import time
from typing import Any


class AssertionMethod:
    @staticmethod
    async def api_response_ok(*args: Any) -> None:
        # Real data is type requests.Response
        assert args[0].ok, f"Error '{args[0].status_code}': {args[0].content}'"

    @staticmethod
    async def empty_value(*args: Any) -> None:
        assert await args[0], f"Value '{args[0]}' should not be empty"

    @staticmethod
    async def false(*args: Any) -> None:
        # args[0] = message
        assert False, args[0]

    @staticmethod
    async def greater_then(*args: Any) -> None:
        assert (
            await args[0] > args[1]
        ), f"Value '{args[0]}' is not greater then {args[1]}"

    @staticmethod
    async def is_checked(*args: Any) -> None:
        assert (
            await args[0].locator(args[1]).is_checked()
        ), f"Locator {args[1]} is not checked"

    @staticmethod
    async def is_empty(*args: Any) -> None:
        assert await args[0], f"Data {args[0]} should not be empty"

    @staticmethod
    async def is_equal(*args: Any) -> None:
        assert (
            await args[0] == args[1]
        ), f"Data '{args[0]}' is not the same as '{args[1]}'"

    @staticmethod
    async def is_in(*args: Any) -> None:
        assert await args[0] in args[1], f"Data '{args[0]}' is not in '{args[1]}'"

    @staticmethod
    async def is_not_none(*args: Any) -> None:
        assert await args[0] is not None, f"Data '{args[0]}' is None"

    @staticmethod
    async def is_not_visible(*args: Any) -> None:
        # Add try/except block for @retry() decorator to work properly
        # args[0]: page
        # args[1]: selector
        # args[2]: assert awaitionMethod.RELOAD
        try:
            assert (
                not await args[0].locator(args[1]).is_visible()
            ), f"Locator '{args[1]}' should not be visible"
        except AssertionError:
            try:
                if args[2]:
                    args[0].reload()
                    raise AssertionError
            except IndexError:
                pass

    @staticmethod
    async def is_visible(*args: Any) -> None:
        # Add try/except block for @retry() decorator to work properly
        # args[0]: page
        # args[1]: selector
        # args[2]: assert awaitionMethod.RELOAD
        try:
            assert (
                await args[0].locator(args[1]).first.is_visible()
            ), f"Locator {args[1]} is not visible"
        except AssertionError:
            try:
                if args[2]:
                    args[0].reload()
            except IndexError:
                assert False, f"Locator {args[1]} is not visible"

    @staticmethod
    async def lesser_than(*args: Any) -> None:
        assert (
            await args[0] < args[1]
        ), f"Value '{args[0]}' is not lesser then '{args[1]}'"

    @staticmethod
    async def not_equal(*args: Any) -> None:
        assert (
            await args[0] != args[1]
        ), f"Data '{args[0]}' is not the same as '{args[1]}'"

    @staticmethod
    async def not_in(*args: Any) -> None:
        assert (
            await args[0] not in args[1]
        ), f"Data '{args[0]}' should not be in '{args[1]}'"

    @staticmethod
    async def wait_for_selector_to_become_visible(*args: Any) -> None:
        try:
            timeout: int = args[2]
        except IndexError:
            timeout = 10
        # locator.is_visible() has deprecated timeout. This is custom implementation
        while timeout > 0:
            if not await args[0].locator(args[1]).first.is_visible():
                timeout -= 1
                time.sleep(1)
            else:
                return
        assert False, f"Locator '{args[1]}' is not in state visible"
