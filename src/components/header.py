from selene.api import *


class Header(object):
    def __init__(self):
        self.account_button = s(by.xpath('//*[@id="gbw"]/div[2]/div/div[2]/div[4]/div[1]/a/span'))