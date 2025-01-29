import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_iphonedemo(playwright: Playwright) -> None:
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context(**playwright.devices["iPhone 13"])
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_iphonedemo(playwright)
