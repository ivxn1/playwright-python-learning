from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://playwright.dev")
        search_button = page.get_by_role(role="button", name='search')
        search_button.click()
        search_input = page.get_by_role(role='searchbox', name='search')
        search_input.type("Python", delay=100)
        page.keyboard.press("Enter")

run()