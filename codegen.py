from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://juice-shop.herokuapp.com/login
    page.goto("https://juice-shop.herokuapp.com/login")

    # Go to https://juice-shop.herokuapp.com/login#/
    page.goto("https://juice-shop.herokuapp.com/login#/")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
