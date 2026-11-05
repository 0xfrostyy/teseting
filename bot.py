import asyncio
from playwright.async_api import async_playwright, TimeoutError


ANSWER = "B"

accounts = [
   


{"username":"sunny-1","wallet":"3HBrdGigUxi3FokCeV6VsY46E744GMgVJPZhg13NyfYf"},
{"username":"sunny-2","wallet":"GEVGkbE4v5vzNXoc1Fid2mBm6oCKq3mxQbE3w9HbfAEK"},
{"username":"sunny-3","wallet":"GpNNbBBLgoPaNNj6V5cWBFUhX43jjdE53VJijvPhFhsu"},
{"username":"sunny-4","wallet":"5cdLqMUwy5okG4aTBwsY6F2uFzSnjfRs3iY8GCrbJ9AT"},
{"username":"sunny-5","wallet":"DRZDT6rW5bZXvJFKrp31bkkS8RxMfx8ktXD381AnyeUq"},
{"username":"sunny-6","wallet":"CfjMTYs6A2MbDiokKBc5CWq8jbcy8iea7tsfw9D6N8Do"},
{"username":"sunny-7","wallet":"DB8r45ai2EgnuxKf13JqbpxrLPxxBF2eJACopC6Er1aH"},
{"username":"sunny-8","wallet":"8RwBhp2Q86SeSWqt8Y2vspR5LfqWmQCdu2wpUTM3cSXS"},
{"username":"sunny-9","wallet":"4q58evjqN3G6ura5t5rqptLPdDVjCFENFTpeGyR5uPnH"},
{"username":"sunny-10","wallet":"B1KVMqniFQ9dJJKxq9wvMXWW91zz8R5Q18TANJfbBVRq"},
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
{"username":"sunny-31","wallet":"589EmKZ8qGWv3yFWMfFVf9pDvMVRKRDVQ9phG9qWCxV8"},
{"username":"sunny-32","wallet":"5skfMMRrtvpkQMUb6UCL8t4pYdXKfePhMVTTBHAA4bbD"},
{"username":"sunny-33","wallet":"Gv8i3FMPdJ34dx8ECrBk7FGjY25znLya3XVqRvQx2kHA"},
{"username":"sunny-34","wallet":"7dZ7hwvdxvdopQphDxjFGcYRSWdjLjyCxS9fcH4HqozN"},
{"username":"sunny-35","wallet":"HM4f4PkYZzKLBRz8Pg7GYJQALkPR2KuPUdj4UGwrCy1u"},
{"username":"sunny-36","wallet":"EzhAiQN6PqaneHFJfJfemiYdmjeERwDdko1gNQK9S4mV"},
{"username":"sunny-37","wallet":"85TMZhoy1vS28MyoTaZoveVYVtzZgs5yFuZBZXDHkkg7"},
{"username":"sunny-38","wallet":"4uAm6uy53nTv4H6oKhbVRVMKwXEGXVHqgyze9UGG5Ezv"},
{"username":"sunny-39","wallet":"7oTDfUMshYtrptiSgNqA7qKjTTykmdLJ3gvPBy6hJoLd"},
{"username":"sunny-40","wallet":"CNmPaJnQmccY6i9idTPJbzpqNCocDGaGsS934QutBbwe"},
{"username":"sunny-41","wallet":"31rBR2ST1UKmbMWX6qPMwsEEpxhdqacFLPsdHsQRStJg"},
{"username":"sunny-42","wallet":"8NTsXRD6WVoUxZ3bNfH2uyfxENPJ7V4868FfuSd217Lv"},
{"username":"sunny-43","wallet":"DMEL3SsNAjm4Lzyx3uSfzcF9A3CaZpqgQE7SeoRBp5o8"},
{"username":"sunny-44","wallet":"9taPHsUksJ14RXTPJPM7gjeE5yHpowSYvXBNrTCP9TeB"},
{"username":"sunny-45","wallet":"76UpjzV9yWYsuhCSBWMRegfK4MZ4pTRCbyW9UpYwhTXz"},
{"username":"sunny-46","wallet":"dTv3RbebvegzCMiyBBMP3XAMoZBoaMDiDDwGSaMhAYM"},
{"username":"sunny-47","wallet":"42xBR3LWgCX8tgDqnsqop5Ro2sfCkPTGKE7ZKzGkQyPv"},
{"username":"sunny-48","wallet":"3oZL7mGAFcNGSN4oibsm2VGGc8562G2uCnmYvvYgRxfP"},
{"username":"sunny-49","wallet":"5RUS1rRHwXJRi6cM73FpKYB7NB3h5Pb6oHmZmmK4DZ9k"},
{"username":"sunny-50","wallet":"4m7MhFqAAGxsSRRwKUJ7tMcXYJAcw8pgt3N6f7ZtdXz3"},


  
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

            await context.close()

        await browser.close()
        print("🎉 All accounts processed successfully!")

if __name__ == "__main__":
    asyncio.run(run_bot())
