from selenium.webdriver.common.by import By
from .base_page import BasePage

class ImdbResultsPage(BasePage):
    FIRST_RESULT = (By.CSS_SELECTOR, '[data-testid="find-results-section-title"] a.ipc-title-link-wrapper')

    def open_first_result(self):
        self.click(self.FIRST_RESULT)
