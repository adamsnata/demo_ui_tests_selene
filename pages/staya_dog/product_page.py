from selene.support.shared import browser
from selene import by, be, query
from locators.pages import product_locators
from pages.base_page import BasePage


class ProductPage(BasePage):
    @staticmethod
    def remember_product():
        product_collection_name = browser.all(by.xpath(product_locators.product_collection_name))[1].get(query.text)
        product_article_name = browser.all(by.xpath(product_locators.product_article_name))[1].get(query.text)
        return product_collection_name, product_article_name

    def select_size(self):
        try:
            browser.all(by.xpath(product_locators.product_size_select))[1].should(be.visible).click()
        except:
            pass

    def add_to_cart(self):
        browser.element(by.xpath(product_locators.add_to_cart_button)).should(be.visible).click()
