from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
# from selenium.webdriver.support.ui import Select


list1,list2 = [],[]

driver = webdriver.Chrome()
# driver.implicitly_wait(5)           ##### implicitly_wait is applied globally every time driver is used

driver.get("https://www.rahulshettyacademy.com/seleniumPractise/")

key = 'ca'

driver.find_element_by_css_selector('.search-keyword').send_keys(key)
time.sleep(4)
count = len(driver.find_elements_by_css_selector('.products div.product'))

assert count == 4

buttons = driver.find_elements_by_css_selector('.product-action button')

# ('//div[@class="product-action"]/button/parent::div/parent::div/h4')            ##### Traversing from child to parent
for btn in buttons:
    list1.append(btn.find_element_by_xpath('parent::div/parent::div/h4').text)
    btn.click()

# print(list1)

driver.find_element_by_css_selector('img[alt="Cart"]').click()

driver.find_element_by_xpath('//button[text()="PROCEED TO CHECKOUT"]').click()

time.sleep(4)
checkedout_products = driver.find_elements_by_xpath('//p[@class="product-name"]')
for chkp in checkedout_products:
    list2.append(chkp.text)
# print(list2)

assert list1 == list2

sum = 0
price1 = driver.find_elements_by_xpath('//table[@class="cartTable"]/tr/td[5]/p')
for p in price1:
    # print(p.text)
    sum += int(p.text)
print(sum)

total_amt = int(driver.find_element_by_css_selector('.totAmt').text)

print(total_amt)

coupon_code = "rahulshettyacademy"

### Explicit wait
wait = WebDriverWait(driver,7)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,'input[class="promoCode"]')))
driver.find_element_by_css_selector('input[class="promoCode"]').send_keys(coupon_code)

driver.find_element_by_class_name("promoBtn").click()



wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,'promoInfo')))
print(driver.find_element_by_class_name("promoInfo").text)
