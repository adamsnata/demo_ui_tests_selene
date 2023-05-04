from selene import by, be
from selene.support.shared import browser
from locators.components import header_menu_locators


class HeaderMenu:
    def press_log_in(self):
        browser.element(by.xpath(header_menu_locators.login_button)).click()

    def check_log_in_button(self):
        browser.element(by.xpath(header_menu_locators.login_button)).should(be.visible)

    def choose_section(self, section):
        browser.element(by.xpath(header_menu_locators.sections.format(text=section))).click()

    def open_profile(self):
        browser.element(by.xpath(header_menu_locators.profile_button)).click()

    def open_cart(self):
        browser.element(by.xpath(header_menu_locators.cart_button)).click()
