from pages.home_page import HomePage
from playwright.sync_api import Page


def test_get_search_results(page: Page):

    home = HomePage(page)
    home.open()
    home.search("Python")

    home.page.wait_for_timeout(1000)

    page.screenshot(path="../../screenshots/day_2_screenshot.png")