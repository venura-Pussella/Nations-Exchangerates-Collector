from playwright.async_api import async_playwright
from src.configuration import configuration

async def fetch_url():
    url = configuration.url
    user_agent = configuration.USER_AGENT

    async with async_playwright() as p:
        # Launch a new browser instance
        browser = await p.firefox.launch()
        
        # Create a new browser context with user-agent
        context = await browser.new_context(user_agent=user_agent)
        
        # Create a new page within this context
        page = await context.new_page()
        
        # Navigate to the URL
        await page.goto(url, timeout=30000)
        
        # Get the content of the page
        content = await page.content()
        
        # Close the browser
        await browser.close()

        return content
