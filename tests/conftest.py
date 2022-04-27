from playwright.sync_api import Browser, Page, sync_playwright
from pytest import fixture


@fixture(scope="session")
def browser() -> Browser:
    browser = sync_playwright().start()
    return browser.chromium.launch(headless=False)


@fixture(scope="session")
def context(browser) -> Browser:
    context = browser.new_context(record_video_dir="records")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context
    context.tracing.stop(path="reports/trace.zip")
    context.storage_state(path="reports/storage.txt")
    context.close()


@fixture(scope="session")
def page(context) -> Page:
    # page: Page = browser.new_page()
    # Record video
    page: Page = context.new_page()
    # page: Page = context.new_page(record_video_dir="records")
    return page


@fixture(scope="session")
def successful_login(page: Page) -> None:
    # Go to https://juice-shop.herokuapp.com/login
    page.goto("https://juice-shop.herokuapp.com/login")
    # Go to https://juice-shop.herokuapp.com/login#/
    page.goto("https://juice-shop.herokuapp.com/login#/")
    # Click [aria-label="Close\ Welcome\ Banner"]
    page.locator("[aria-label=\"Close\\ Welcome\\ Banner\"]").click()
    # Click [aria-label="Show\/hide\ account\ menu"]
    page.locator("[aria-label=\"Show\\/hide\\ account\\ menu\"]").click()
    # Click button[role="menuitem"]:has-text("exit_to_app Login")
    page.locator("button[role=\"menuitem\"]:has-text(\"exit_to_app Login\")").click()
    assert page.url == "https://juice-shop.herokuapp.com/login#/login"
    # Click #login-form div:has-text("Email *") >> nth=2
    page.locator("#login-form div:has-text(\"Email *\")").nth(2).click()
    # Fill [aria-label="Text\ field\ for\ the\ login\ email"]
    page.locator("[aria-label=\"Text\\ field\\ for\\ the\\ login\\ email\"]").fill("jaksa.milanovic007@gmail.com")
    # Click [aria-label="Text\ field\ for\ the\ login\ password"]
    page.locator("[aria-label=\"Text\\ field\\ for\\ the\\ login\\ password\"]").click()
    # Fill [aria-label="Text\ field\ for\ the\ login\ password"]
    page.locator("[aria-label=\"Text\\ field\\ for\\ the\\ login\\ password\"]").fill("Test123*")
    # Click [aria-label="Login"]
    page.locator("[aria-label=\"Login\"]").click()
