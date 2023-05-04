from selene.support.shared import browser
from selene import by, have
from locators.pages import profile_locators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    def check_orders_exists(self):
        browser.element(by.xpath(profile_locators.my_orders)).should(have.text("Мои заказы"))

    def log_out(self):
        browser.element(by.xpath(profile_locators.logout_button)).click()

    def log_out_submit(self):
        browser.element(by.xpath(profile_locators.logout_button_submit)).click()
