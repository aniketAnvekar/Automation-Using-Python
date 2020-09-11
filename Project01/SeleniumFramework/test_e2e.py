from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
from BaseClass import BaseClass1
from pageObjects.homePage import HomePage
from pageObjects.checkout import CheckOut


class TestApp(BaseClass1):
    def test_e2e(self):
        homepage = HomePage(self.driver)
        checkoutobj = homepage.clickShop()
        products = checkoutobj.getProducts()
        i = -1
        for product in products:
            i += 1
            if product.text == "Samsung Note 8":
                checkoutobj.getFooter()[i].click()
                break

        checkoutobj.checkMeOut().click()

        confirmPageObj = checkoutobj.checkMeAgain()
        # self.driver.find_element_by_css_selector('button.btn.btn-success').click()

        confirmPageObj.addCountry()
        # self.driver.find_element_by_css_selector('input[id="country"]').send_keys("ind")


        # wait = WebDriverWait(self.driver,8)
        #
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
        #
        # self.driver.find_element_by_link_text("India").click()
        #
        # self.driver.find_element_by_css_selector("div.checkbox.checkbox-primary").click()
        #
        # self.driver.find_element_by_css_selector('input[type="submit"]').click()
        #
        # print(self.driver.find_element_by_css_selector('div.alert-success').text)

        confirmPageObj.placeOrder()
