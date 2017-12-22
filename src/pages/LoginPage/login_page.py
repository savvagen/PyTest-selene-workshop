from selene.api import *
from src.pages.MainPage.main_page import MainPage


class LoginPage(object):
    def __init__(self):
        self.email_field = s(by.name("identifier"))
        self.password_field = s(by.name("password"))
        self.email_error = s(by.xpath('//*[@id="view_container"]/form/div[2]/div/div[1]/div[1]/div/div[2]/div[2]'))
        self.password_error = s(by.xpath('//*[@id="password"]/div[2]/div[2]'))
        self.next_button = s(by.text("Далее"))

    def login_as(self, user):
        self.email_field.set(user.email)
        self.next_button.click()
        self.password_field.set(user.password).press_enter()
        return MainPage()
