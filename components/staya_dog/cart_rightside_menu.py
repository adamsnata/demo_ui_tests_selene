from selene import by, be
from selene.support.shared import browser

from locators.components import cart_rightside_locators


class CartRightSideMenu:

    def submit_checkout(self):
        browser.element(by.xpath(cart_rightside_locators.cart_checkout_button)).should(be.visible).click()
