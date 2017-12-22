from selene.api import *


class SearchResults(object):
    def __init__(self):
        self.results = ss(".srg .g")

    def get(self, index):
        return SearchResult(index)


class SearchResult(object):
    def __init__(self, index):
        self.results = SearchResults()
        self.result = SearchResults().results[index - 1]

    def result_title(self):
        return self.result.s(by.css("h3 a"))
