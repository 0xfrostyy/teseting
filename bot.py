import asyncio
from playwright.async_api import async_playwright, TimeoutError


ANSWER = "C"

accounts = [
{"username":"sunny-21","wallet":"A34h5FbvH6TfWom2cp2i5pRUz8ZbkKUkPxbxhGMNck59"},
{"username":"sunny-22","wallet":"GTXTaJ4sMhE5sipURRVPdTocKgXmb9mM7xFDunH488pK"},
{"username":"sunny-23","wallet":"83LgTnuin78pM1b3Y1JF8TrwKkLR6oCGp3tNAkNbHJc2"},
{"username":"sunny-24","wallet":"J6NXugETAUgRgULCGBKZ1YkGZ2LsL4EnUeaorxmY2Xq2"},
{"username":"sunny-25","wallet":"E9oJnwkLCwPXrDv4vWmdRo7jkf1BFnrQcLhWQ2cZw7XC"},
{"username":"sunny-26","wallet":"FeseCBBgMd8tB8MYUZysbsCStrusMTkMpoy8FsFC6nHe"},
{"username":"sunny-27","wallet":"DPoYdv2c4S2ec4fhd3c2fvBT71ACRK21CFWVfZ68pgD4"},
{"username":"sunny-28","wallet":"D8XR7yoNjU2fiLDqfM2ughjBGRcZq8bQyyZF5WXq8zby"},
{"username":"sunny-29","wallet":"Ddx3o5Kq1DdScnRYg9xvRs2vC7Fs4XLpTZearWTNo9wm"},
{"username":"sunny-30","wallet":"4gdqfyyx52aVKZuFhHhBNhsRM9AT5vBhD5jrjEF87Nta"},



]

async def handle_modal(page):
    modal = page.locator("#scamMigrationWarningModal")
    try:
        if await modal.is_visible(timeout=5000):
            print("⚠️ Closing modal...")
            buttons = modal.locator("button")
            if await buttons.count() > 0:
                await buttons.first.click()
                await page.wait_for_timeout(1000)
    except:
        pass

async def run_bot():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )

        for acc in accounts:
            context = await browser.new_context()
            page = await context.new_page()

            print("Running account:", acc["username"])

            try:
                await page.goto("https://theros.io/prelaunch", timeout=80000)
                await page.wait_for_load_state("networkidle", timeout=15000)
            except TimeoutError:
                print(f"Timeout for {acc['username']}. Skipping.")
                await context.close()
                continue

            await handle_modal(page)
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            await page.wait_for_selector("input", timeout=15000)

            inputs = await page.query_selector_all("input")
            if len(inputs) < 2:
                print(f"Not enough inputs for {acc['username']}, skipping")
                await context.close()
                continue

            await inputs[0].fill(acc["username"])
            await inputs[1].fill(acc["wallet"])

            if len(inputs) > 2:
                await inputs[2].fill("bot")

            await handle_modal(page)

            create_btn = page.locator("#registerBtn")
            try:
                await create_btn.click(timeout=9000)
            except TimeoutError:
                await create_btn.click(force=True)

            next_btn = page.locator("#nextQuestionBtn")
            try:
                await next_btn.wait_for(state="visible", timeout=8000)
                await next_btn.click()
            except:
                pass

            answer_selector = f"#answer{ANSWER.upper()}"
            try:
                await page.locator(answer_selector).click(timeout=20000)
                print("Answered:", ANSWER)
            except Exception as e:
                print(f"Failed to answer: {e}")

            await page.wait_for_timeout(10000)
            await context.close()

        await browser.close()
        print("🎉 All accounts processed successfully!")

if __name__ == "__main__":
    asyncio.run(run_bot())
