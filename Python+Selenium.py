from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()


'''3.Filling input fields using selenium'''
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
'''One input field'''
messageBox = driver.find_element_by_xpath('//*[@id="user-message"]')

messageBox.send_keys('Hijo de puta')

displayButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')

displayButton.click()

'''Two input field'''
msgBox1 = driver.find_element_by_xpath('//*[@id="sum1"]')
msgBox1.send_keys('250')

msgBox2 = driver.find_element_by_xpath('//*[@id="sum2"]')
msgBox2.send_keys('150')

getTotal = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
getTotal.click()



'''2.Drag and drop using selenium'''
driver.get('http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

element_to_drag = driver.find_element_by_xpath('//*[@id="box3"]')

dest_to_drop = driver.find_element_by_xpath('//*[@id="box103"]')

actions = ActionChains(driver)

actions.drag_and_drop(element_to_drag,dest_to_drop).perform()


'''3.Exploring wait function using selenium'''
driver.get('https://www.google.com/intl/en_in/earth/')
wait = WebDriverWait(driver,10)

lauchEarthButton = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[2]/div/div[3]/div/a')))
lauchEarthButton.click()

# alternate way
# lauchEarthButton = wait.until(lambda driver: driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/a'))
