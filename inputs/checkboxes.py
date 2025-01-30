# to run this: python3 inputs/checkboxes.py
import asyncio
from playwright.async_api import async_playwright, expect

async def test_checkboxes():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        await page.set_viewport_size({"width": 1800, "height": 1200})
        await page.goto("https://demoqa.com/checkbox")
        
        # Actions
        await page.check('label[for="tree-node-home"]')
        await page.screenshot(path="screenshots/checkboxes.png")
        
        # Assertions
        assert await page.is_checked('label[for="tree-node-home"]') is True
        await expect(page.locator("#result")).to_have_text(
            "You have selected :homedesktopnotescommandsdocumentsworkspacereactangularveuofficepublicprivateclassifiedgeneraldownloadswordFileexcelFile"
        )
        
        # Stopping Tracing
        await context.tracing.stop(path="logs/trace.zip")
        
        # Closing browser
        await browser.close()

asyncio.run(test_checkboxes())