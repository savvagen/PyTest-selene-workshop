from selene.api import *
from src.pages.SearchPage.components.search_results import SearchResults
from src.pages.LoginPage.login_page import LoginPage

class SearchPage(object):
    def __init__(self):
        self.url = "/"
        self.search_field = s(by.name("q"))
        self.login_button = s(by.text("Войти"))

    def open(self):
        browser.open_url(self.url)
        return self

    def search(self, text):
        self.search_field.set(text).press_enter()
        return SearchResults()

    def press_login(self):
        self.login_button.click()
        return LoginPage()

