pytest_plugins: list = [
    "tests.fixtures.clean_up",
    "tests.fixtures.docker",
    "tests.fixtures.pages",
    "tests.fixtures.playwright",
    "tests.fixtures.trace",
    "tests.fixtures.register",
]

pytest_plugins.insert(0, "tests.fixtures.docker")
