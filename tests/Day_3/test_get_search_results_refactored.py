# Here pytest is used rather than directly running the program, having refactored the code from Day_2...

from playwright.sync_api import Page

def test_get_search_results(page: Page):
    page.goto("https://playwright.dev/")

    page.goto(url="https://playwright.dev/")

    search_button = page.get_by_role(role='button', name="Search")
    search_button.click()
    search_box = page.get_by_role(role='searchbox', name='Search')
    search_box.type("Python", delay=300)
    page.keyboard.press("Enter")

    page.wait_for_timeout(1000)

    page.screenshot(path="../../screenshots/day_2_screenshot.png")