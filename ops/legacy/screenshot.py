import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.setViewport({'width': 1920, 'height': 1080})
    await page.goto('http://localhost:8000')
    await asyncio.sleep(2)  # wait for loader to render
    await page.screenshot({'path': 'loader-desktop.png'})
    
    await page.setViewport({'width': 375, 'height': 812})
    await page.goto('http://localhost:8000')
    await asyncio.sleep(2)
    await page.screenshot({'path': 'loader-mobile.png'})
    
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
