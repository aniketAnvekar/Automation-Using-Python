from selenium.webdriver.common.by import By
from pageObjects.confirmPage import ConfirmPage

class CheckOut:
    def __init__(self,driver):
        self.driver = driver

    products = (By.CSS_SELECTOR,'app-card-list.row div.card.h-100')
    footer = (By.CSS_SELECTOR,'div.card-footer button')
    checkout = (By.CSS_SELECTOR,'a.nav-link.btn.btn-primary')
    checkmeagain = (By.CSS_SELECTOR,'button.btn.btn-success')

    def getProducts(self):
        return self.driver.find_elements(*CheckOut.products)

    def getFooter(self):
        return self.driver.find_element(*CheckOut.footer)

    def checkMeOut(self):
        # self.driver.find_element_by_css_selector('a[href*="shop"]').click()
        return self.driver.find_element(*CheckOut.checkout)

    def checkMeAgain(self):
        self.driver.find_element(*CheckOut.checkmeagain).click()
        confirmPageObj = ConfirmPage(self.driver)
        return confirmPageObj
