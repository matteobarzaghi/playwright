import re
from playwright.sync_api import sync_playwright, expect

def test_login():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=1500)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")
        page.locator("[data-test=\"username\"]").fill("standard_user")
        page.locator("[data-test=\"password\"]").fill("secret_sauce")
        page.locator("[data-test=\"login-button\"]").click()

        # Verifica che il login sia riuscito controllando un elemento della dashboard
        expect(page.locator(".inventory_list")).to_be_visible()

        context.close()
        browser.close()

