import asyncio
from playwright.async_api import async_playwright, TimeoutError


ANSWER = "C"

accounts = [
{"username":"sunny-11","wallet":"CJgNKqns6h66cJt2NNZM6Rb1ue2c2wDeMVjgtunPmHAo"},
{"username":"sunny-12","wallet":"EMWnfG5BqNqXJR8VR4YhJ6bPb1yjmyrk3MwKsAwgYCxC"},
{"username":"sunny-13","wallet":"BDjM5H5s2G6S8EVphh4Wzyhfw6dov2GZjh4FqL7UB5F5"},
{"username":"sunny-14","wallet":"775NEWELsmmGSWYK4bUSNyTtPCueLBWy3AbnHich6tz4"},
{"username":"sunny-15","wallet":"ppRNPXeFiJfp7Ncw3bbzmjFeVp8WMD9S16qRKgf5Rf1"},
{"username":"sunny-16","wallet":"8YoY7JShz2rz39hhoTLMbF3hNoDfnVS8gGRS4p4WNyUY"},
{"username":"sunny-17","wallet":"FpqfMAD1GmFaWXqKRJ33nRHgew7pknqwMbGAzYmyismb"},
{"username":"sunny-18","wallet":"KqsVzzf7uR2iwvmTNM48HGjV2gtRdk21bp1CqLBCwQk"},
{"username":"sunny-19","wallet":"9YmSsm6yQWtDxAyCbt1kMGmwF6usJTEzccBT5Hdj2cpT"},
{"username":"sunny-20","wallet":"H8wvxMmb2Hq4RRtPL5TTmZrQqPPxejKz8dnTu5TFZbXr"},


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

            await page.wait_for_timeout(5000)
            await context.close()

        await browser.close()
        print("🎉 All accounts processed successfully!")

if __name__ == "__main__":
    asyncio.run(run_bot())
