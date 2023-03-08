pytest_plugins: list = [
    "tests.fixtures.docker",
    "tests.fixtures.login",
    "tests.fixtures.pages",
    "tests.fixtures.playwright",
    "tests.fixtures.trace"
]

pytest_plugins.insert(0, "tests.fixtures.docker")
