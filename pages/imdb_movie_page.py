from selenium.webdriver.common.by import By
from .base_page import BasePage

class ImdbMoviePage(BasePage):
    TITLE = (By.CSS_SELECTOR, '[data-testid="hero__primary-text"]')
    RATING = (By.CSS_SELECTOR, '[data-testid="hero-rating-bar__aggregate-rating__score"] span')

    def get_title(self):
        return self.find_element(self.TITLE).text

    def get_rating(self):
        for element in self.find_elements(self.RATING):
            rating = element.get_attribute("textContent").strip()
            if rating:
                return rating
        return ""

    def is_rating_valid(self):
        rating = float(self.get_rating().replace(",", "."))
        return 0 < rating <= 10
