import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://example.com", wait_until="networkidle")
        await asyncio.sleep(2)
        await page.screenshot(path="screenshot.png", full_page=True)
        await browser.close()

asyncio.run(run())
