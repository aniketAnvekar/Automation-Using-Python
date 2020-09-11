from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class ConfirmPage:
    def __init__(self,driver):
        self.driver = driver

    searchBox = (By.CSS_SELECTOR,'input[id="country"]')
    clickCheckbox = (By.CSS_SELECTOR,'div.checkbox.checkbox-primary')
    finalSubmit = (By.CSS_SELECTOR,'input[type="submit"]')

    def addCountry(self):
        self.driver.find_element(*ConfirmPage.searchBox).send_keys("ind")

        wait = WebDriverWait(self.driver,8)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
        self.driver.find_element_by_link_text("India").click()

    def placeOrder(self):
        self.driver.find_element(*ConfirmPage.clickCheckbox).click()
        self.driver.find_element(*ConfirmPage.finalSubmit).click()
