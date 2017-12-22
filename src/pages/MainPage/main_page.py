from selene.api import *
from src.components.header import Header


class MainPage(object):
    def __init__(self):
        self.header = Header()
        self.account_button = s(by.xpath('//*[@id="gbw"]/div[2]/div/div[2]/div[4]/div[1]/a/span'))
