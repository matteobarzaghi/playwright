from playwright.sync_api import sync_playwright

# use the sync_playright library with the alias p
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://whatmyuseragent.com/")
    page.screenshot(path="demo.png")
    browser.close()