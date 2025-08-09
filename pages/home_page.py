from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_button = page.get_by_role(role="button", name="Search")

    def open(self):
        self.page.goto("https://playwright.dev")

    def search(self, keyword: str):
        self.search_button.click()
        search_input = self.page.get_by_role(role="searchbox", name='Search')
        search_input.type(keyword, delay=100)
        self.page.keyboard.press("Enter")

