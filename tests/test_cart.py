import allure
from app import app
from allure_commons.types import Severity


class TestAddToCart:
    @allure.parent_suite("Web")
    @allure.severity(Severity.NORMAL)
    @allure.suite("Cart")
    @allure.title("Adding a product to cart")
    def test_add_to_cart(self):
        app.base.open_main_page()

        with allure.step('Goto Catalog'):
            app.header_menu.choose_section("Каталог")

        with allure.step('Choose product'):
            app.catalog.choose_products_in_stock()
            app.catalog.choose_random_product()
            collection_name, article_name = app.product.remember_product()

        with allure.step('Choose size'):
            app.product.select_size()

        with allure.step('Add to card'):
            app.product.add_to_cart()

        with allure.step('Goto card'):
            app.rightside_cart.submit_checkout()

        with allure.step('Check card'):
            app.checkout.assert_product_in_cart(collection_name, 'Nata')


class TestClearCart:
    @classmethod
    def setup_class(cls):
        app.base.open_main_page()

        with allure.step('ADd item to card'):
            app.header_menu.choose_section("Каталог")

            app.catalog.choose_products_in_stock()
            app.catalog.choose_random_product()

            app.product.select_size()

            app.product.add_to_cart()

            app.rightside_cart.submit_checkout()

            app.base.open_main_page()

    @allure.parent_suite("Web")
    @allure.severity(Severity.NORMAL)
    @allure.suite("Cart")
    @allure.title("Clearing a cart")
    def test_clear_cart(self):
        with allure.step('Open Cart'):
            app.header_menu.open_cart()
        with allure.step('Go to card'):
            app.rightside_cart.submit_checkout()

        with allure.step('Clean card'):
            app.checkout.clear_the_cart()
        with allure.step('Check Card'):
            app.checkout.assert_the_cart_is_emply()
