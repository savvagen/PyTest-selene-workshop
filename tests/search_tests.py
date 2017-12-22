from src.pages.SearchPage.search_page import SearchPage
from hamcrest import *
from selene.api import *
from selene import config
import pytest
from src.test_data.search_data import searchdata


@pytest.yield_fixture(scope="session", autouse=True)
def set_up_test():
    config.timeout = 10
    yield
    browser.close()


class TestSearch(object):

    @pytest.mark.positive
    def test_positive_search(self):
        search_results = SearchPage().open().search("Selenium")
        search_results.get(1).result_title().should(have.text("Selenium"))
        assert_that(search_results.get(1).result_title().text, contains_string('Selenium'))
        assert_that(len(search_results.results), greater_than(5))

    @pytest.mark.parametrize("text,result", searchdata)
    def test_parametrized_search(self, text, result):
        search_results = SearchPage().open().search(text)
        search_results.get(1).result_title().should(have.text(result))
        assert_that(search_results.get(1).result_title().text, contains_string(result))
        assert_that(len(search_results.results), greater_than(5))
