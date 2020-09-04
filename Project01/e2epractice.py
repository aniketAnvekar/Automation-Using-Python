from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()

driver.get('https://www.rahulshettyacademy.com/angularpractice/')

driver.find_element_by_css_selector('a[href*="shop"]').click()

products = driver.find_elements_by_css_selector('app-card-list.row div.card.h-100')

for product in products:
    p = product.find_element_by_css_selector('h4 a')
    if p.text == "Samsung Note 8":
        product.find_element_by_css_selector('div.card-footer button').click()
        driver.find_element_by_css_selector('a.nav-link.btn.btn-primary').click()
        break


driver.find_element_by_css_selector('button.btn.btn-success').click()

driver.find_element_by_css_selector('input[id="country"]').send_keys("ind")
wait = WebDriverWait(driver,8)

wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))

driver.find_element_by_link_text("India").click()

driver.find_element_by_css_selector("div.checkbox.checkbox-primary").click()

driver.find_element_by_css_selector('input[type="submit"]').click()

print(driver.find_element_by_css_selector('div.alert-success').text)
