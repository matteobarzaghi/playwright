import asyncio
from models.search import SearchPage
from playwright.async_api import async_playwright

async def main():
    # Use the asynchronous context manager
    async with async_playwright() as p:
        # Await launching the browser
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        # Create the SearchPage instance and perform actions
        search_page = SearchPage(page)
        await search_page.navigate()
        await search_page.search("search query")
        
        # Optionally, close the browser
        await browser.close()

# Run the async main function
asyncio.run(main())