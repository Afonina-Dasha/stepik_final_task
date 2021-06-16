from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage

#класс MainPage является наследником класса BasePage(класс предок указ-я. в скобках)
class MainPage(BasePage):
#указываем self чтобы иметь доступ к атрибутам и методам класса:
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"