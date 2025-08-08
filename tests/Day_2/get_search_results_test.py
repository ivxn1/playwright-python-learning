from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url="https://playwright.dev/")

        search_input = page.get_by_role(role='button', name="Search")
        search_input.click()
        search_input.type("Python", delay=300)
        page.keyboard.press("Enter")

        page.screenshot(path="../screenshots/search_results.png")
        browser.close()

if __name__ == "__main__":
    run()
