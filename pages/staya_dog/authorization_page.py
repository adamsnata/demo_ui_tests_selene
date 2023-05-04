from selene.support.shared import browser
from selene import by

from pages.base_page import BasePage
from locators.pages import authorization_locators


class AuthorizationPage(BasePage):
    def type_email(self, email):
        browser.all(by.xpath(authorization_locators.input_email)).first.type(email)

    def type_password(self, password):
        browser.all(by.xpath(authorization_locators.input_password)).first.type(password)

    def submit_log_in(self):
        browser.element(by.xpath(authorization_locators.submit_button)).click()
