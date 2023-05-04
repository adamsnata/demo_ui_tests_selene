import allure
from allure_commons.types import Severity

from app import app
from data.auth_data import StayaAuth


class TestAuthorization:
    @allure.parent_suite("Web")
    @allure.severity(Severity.CRITICAL)
    @allure.suite("Authorization")
    @allure.title("Log in to system")
    def test_authorization(self):
        staya_auth = StayaAuth.get_auth()
        app.base.open_main_page()

        with allure.step('Press log in button'):
            app.header_menu.press_log_in()

        with allure.step('Type email'):
            app.auth.type_email(staya_auth['email'])

        with allure.step('Type password'):
            app.auth.type_password(staya_auth['password'])

        with allure.step('Press submit button'):
            app.auth.submit_log_in()

        with allure.step('Check that orders page exists'):
            app.profile.check_orders_exists()


class TestLogout:
    @allure.parent_suite("Web")
    @allure.severity(Severity.CRITICAL)
    @allure.suite("Authorization")
    @allure.title("Log out from system")
    def test_logout(self):
        app.base.open_main_page()
        with allure.step('Open profile'):
            app.header_menu.open_profile()

        with allure.step('Log out from account'):
            app.profile.log_out()

        with allure.step('Submit logging out'):
            app.profile.log_out_submit()

        with allure.step('Check that log in button is available'):
            app.header_menu.check_log_in_button()
