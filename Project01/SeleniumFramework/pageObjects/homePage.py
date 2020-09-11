from selenium.webdriver.common.by import By
from pageObjects.checkout import CheckOut



class HomePage:
    def __init__(self,driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR,'a[href*="shop"]')

    def clickShop(self):
        # self.driver.find_element_by_css_selector('a[href*="shop"]').click()
        self.driver.find_element(*HomePage.shop).click()
        checkoutobj = CheckOut(self.driver)
        return checkoutobj
