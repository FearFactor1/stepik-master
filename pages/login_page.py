from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage, LoginPageLocators):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#id_login-username")
        assert self.is_element_present(By.CSS_SELECTOR, "#id_login-password")
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#id_registration-email")
        assert self.is_element_present(By.CSS_SELECTOR, "#id_registration-password1")
        assert self.is_element_present(By.CSS_SELECTOR, "#id_registration-password2")
        assert True