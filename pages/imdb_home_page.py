from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class ImdbHomePage(BasePage):
    SEARCH_FIELD = (By.ID, "suggestion-search")
    SEARCH_BTN = (By.ID, "suggestion-search-button")

    def search(self, movie):
        self.enter_text(self.SEARCH_FIELD, movie)
        self.click(self.SEARCH_BTN)
