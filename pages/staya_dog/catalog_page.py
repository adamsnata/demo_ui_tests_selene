from selene.support.shared import browser
from selene import by, have, be
from locators.pages import catalog_locators
from pages.base_page import BasePage
import random


class CatalogPage(BasePage):
    def choose_collection(self, collection_name):
        browser.element(by.xpath(catalog_locators.filter_wrapper)).should(be.visible)
        browser.element(by.xpath(catalog_locators.collections.format(text=collection_name))).click()

    def assert_collection(self, collection_name):
        browser.all(by.xpath(catalog_locators.name_of_title)).first.wait_until(lambda e: e.text == collection_name)

        elements = browser.all(by.xpath(catalog_locators.name_of_title))

        for element in elements:
            element.should(have.text(collection_name))

    def choose_new_products(self):
        browser.element(by.xpath(catalog_locators.filter_wrapper)).should(be.visible)
        browser.all(by.xpath(catalog_locators.tags_checkbox))[2].click()

    def assert_new_products(self):
        browser.all(by.xpath(catalog_locators.product_tags_common)).first.wait_until(lambda e: e.text == 'Новинка')

        elements = browser.all(by.xpath(catalog_locators.product_tags_common))

        for element in elements:
            element.should(have.text('Новинка'))

    def choose_charity_products(self):
        browser.element(by.xpath(catalog_locators.filter_wrapper)).should(be.visible)
        browser.all(by.xpath(catalog_locators.tags_checkbox))[1].click()

    def assert_charity_products(self):
        browser.all(by.xpath(catalog_locators.product_tags_accent)).first.wait_until(
            lambda e: e.text == '5% в «Добро Вместе»')

        elements = browser.all(by.xpath(catalog_locators.product_tags_accent))

        for element in elements:
            element.should(have.text('5% в «Добро Вместе»'))

    def choose_random_product(self):
        browser.element(by.xpath(catalog_locators.product_list)).should(be.visible)
        browser.all(by.xpath(catalog_locators.product_list))[random.randint(1, 19)].click()

    def choose_products_in_stock(self):
        browser.element(by.xpath(catalog_locators.filter_wrapper)).should(be.visible)
        browser.all(by.xpath(catalog_locators.tags_checkbox))[0].click()
