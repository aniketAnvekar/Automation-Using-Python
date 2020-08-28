from selenium import webdriver
# import time
# from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()

####################    Using Selenium on sample form    #############################

# driver.get('https://www.rahulshettyacademy.com/angularpractice/')

# print(driver.title)
# print(driver.current_url)

# driver.find_element_by_css_selector('input[name="name"]').send_keys("Walter White")         # Filling textboxi.e name

# driver.find_element_by_xpath('//input[@name="email"]').send_keys("callmefor@meth.com")      # Filling email

# driver.find_element_by_css_selector('#exampleInputPassword1').send_keys("Kingpin")          # Password

# driver.find_element_by_id("exampleCheck1").click()                                          # click chechbox

# dropdown = Select(driver.find_element_by_xpath('//select[@id="exampleFormControlSelect1"]'))   # dropdown
# dropdown.select_by_visible_text('Female')       # selecting by value present in the dropdown
# dropdown.select_by_index(0)                     # selecting by index of the value present in the dropdown

# driver.find_element_by_css_selector('#inlineRadio2').click()                                # clicking radio button

# driver.find_element_by_xpath('//input[@name="bday"]').send_keys("28-08-2020")             # Selecting date

# driver.find_element_by_xpath('//input[@type="submit"]').click()                             # clicking submit buuton

# data = driver.find_element_by_class_name('alert-success').text                              # storing success message
# assert 'success' in data

# driver.close()


####################    Using Selenium on Salesforce login form     #############################

########  Generating css from id  ########
# tagname#id

########  Generating css from class  ########
# tagname.className

# driver.get('https://login.salesforce.com/')

# driver.find_element_by_css_selector('#username').send_keys('hello')     #### by id tag
# or
# driver.find_element_by_css_selector('.username').send_keys('hello')      ##### by class tag

# driver.find_element_by_css_selector('#password').send_keys('yeahyeah!!!')

# driver.find_element_by_css_selector('#password').clear()

# driver.find_element_by_link_text('Forgot Your Password?').click()       #### to access a link closed under a tag

# driver.find_element_by_xpath('//a[text()="Cancel"]').click()             #### to access a link using xpath: ('//tag[text()="text"]')

###### Understanding parent-child hierarchy #######

# print(driver.find_element_by_xpath('//form[@id="login_form"]/div[1]/label').text)         #### Xpath syntax to get the child

# print(driver.find_element_by_css_selector('form[id="login_form"] label:nth-child(2)').text)   #### CSS syntax to get the child



######################    Using Selenium on Flight Booking Portal    #############################

# driver.get('https://rahulshettyacademy.com/dropdownsPractise/')
#
# driver.find_element_by_id('autosuggest').send_keys('chi')
#
# time.sleep(2)
#
# locations = driver.find_elements_by_css_selector('li[class="ui-menu-item"] a')
# # or use ('.ui-autocomplete li a')
#
# for l in locations:
#     if l.text == "Taiwan, Province of China":
#         l.click()
#         break
#
# assert driver.find_element_by_id('autosuggest').get_attribute('value') == "Taiwan, Province of China"


######################################################################################################

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

chechboxes = driver.find_elements_by_xpath('//input[@type="checkbox"]')

option = ['option1','option2']

def isPresent(value):
    for opt in option:
        if opt == value:
            return True
    return False

for checkbox in chechboxes:
    if isPresent(checkbox.get_attribute("value")):
        checkbox.click()
        assert checkbox.is_selected()




# label = driver.find_elements_by_css_selector('div[id="checkbox-example"] label')
# for l in label:
#     print(l.text)
