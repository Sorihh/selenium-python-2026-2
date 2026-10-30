from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class LobbyLoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "username")
    LOGIN_BTN = (By.ID, "btn-login")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")

    def login(self, username):
        self.enter_text(self.USERNAME_FIELD, username)
        self.click(self.LOGIN_BTN)

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text
    
    def is_login_form_displayed(self):
        return self.find_element(self.USERNAME_FIELD).is_displayed()