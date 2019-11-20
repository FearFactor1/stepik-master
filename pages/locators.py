from selenium.webdriver.common.by import By

class LoginPageLocators():
    REGISTER_EMAIL_ADDRESS = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    LOG_IN_EMAIL_ADDRESS = (By.CSS_SELECTOR, "#id_login-username")
    LOG_IN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    FINISH_TEXT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_TEXT = (By.CSS_SELECTOR, "div.col-sm-6:nth-child(2) > h1:nth-child(1)")
    PRICE_BASKET = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LOOK_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > a:nth-child(1)")
    TEXT_IN_BASKET = (By.CSS_SELECTOR, "#content_inner > p:nth-child(1)")
    PRODUCTS_LINK = (By.CSS_SELECTOR, ".dropdown > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)")
    EMAIL_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASSWORD_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password2")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    ENTER = (By.CSS_SELECTOR, "#login_link")