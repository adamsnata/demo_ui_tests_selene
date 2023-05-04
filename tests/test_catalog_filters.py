import allure
from allure_commons.types import Severity

from app import app


class TestCollectionProducts:
    @allure.parent_suite("Web")
    @allure.severity(Severity.MINOR)
    @allure.suite("Filters")
    @allure.title("Collections is visible")
    def test_collections(self):
        app.base.open_main_page()
        with allure.step('Goto Catalog'):
            app.header_menu.choose_section("Каталог")
        with allure.step('Choose Kollektions'):
            app.catalog.choose_collection("Mono Yellow")
        with allure.step('Check Kollektions'):
            app.catalog.assert_collection("Mono Yellow")


class TestNewProducts:
    @allure.parent_suite("Web")
    @allure.severity(Severity.TRIVIAL)
    @allure.suite("Filters")
    @allure.title("New products is visible")
    def test_new_products(self):
        app.base.open_main_page()
        with allure.step('Go to Catalog'):
            app.header_menu.choose_section("Каталог")
        with allure.step('Choose New'):
            app.catalog.choose_new_products()
        with allure.step('Check is visible new'):
            app.catalog.assert_new_products()


class TestCharityProducts:
    @allure.parent_suite("Web")
    @allure.severity(Severity.TRIVIAL)
    @allure.suite("Filters")
    @allure.title("Charity products is visible")
    def test_charity_products(self):
        app.base.open_main_page()
        with allure.step('Go to Catalog'):
            app.header_menu.choose_section("Каталог")
        with allure.step('choose'):
            app.catalog.choose_charity_products()
        with allure.step('Check togethe'):
            app.catalog.assert_charity_products()
