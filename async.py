import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://whatmyuseragent.com/")
        print(await page.title())
        browser.close()

asyncio.run(main())