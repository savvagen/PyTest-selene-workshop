from selene.conditions import *
from src.account.user import User
from src.pages.LoginPage.login_page import LoginPage
import pytest
from selene import config
from selene.api import *
from src.pages.SearchPage.search_page import SearchPage


@pytest.yield_fixture(scope="session", autouse=True)
def set_up_test():
    config.timeout = 10
    SearchPage().open().press_login()
    yield
    browser.close()


def test_positive_login():
    test_user = User("genchevskiy.test@gmail.com", "s.g19021992")
    main_page = LoginPage().login_as(test_user)
    main_page.header.account_button.should_be(visible, 10)

