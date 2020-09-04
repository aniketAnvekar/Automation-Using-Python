from selenium import webdriver

driver = webdriver.Chrome()

# driver.get("https://the-internet.herokuapp.com/windows")
#
# driver.find_element_by_link_text("Click Here").click()
#
# # page id's are stored in the form of [parent_page_id, child_page1_id, child_page2_id, ....,child_pageN_id]
# child_id1 = driver.window_handles[1]
# driver.switch_to_window(child_id1)
#
# print(driver.find_element_by_tag_name("h3").text)
# # driver.close()          ### to close child windows
#
# driver.switch_to_window(driver.window_handles[0])           ### Going back to home page
#
# driver.find_element_by_link_text("Elemental Selenium").click()
#
# child_id2 = driver.window_handles[2]        ### If first child wimdow is closed then index will be 1
# driver.switch_to_window(child_id2)
#
# print(driver.find_element_by_tag_name("h1").text)
# # driver.close()          ### to close child windows
#
# driver.switch_to_window(driver.window_handles[0])
#
# print(driver.find_element_by_tag_name("h3").text)



######################  Working with frames #########################

# driver.get('https://the-internet.herokuapp.com/frames')
#
# driver.find_element_by_link_text("iFrame").click()
#
# driver.switch_to_frame("mce_0_ifr")
#
# # enter the frame
# frame = driver.find_element_by_id('tinymce')
#
# frame.clear()
# frame.send_keys("I am able to automate")
#
# driver.switch_to_default_content()          # leave the frame
#
# print(driver.find_element_by_tag_name("h3").text)




######################  Working with mouse hover icon #########################
# from selenium.webdriver import ActionChains
#
# driver.get('https://rahulshettyacademy.com/AutomationPractice/')
#
# action = ActionChains(driver)
#
# menu = driver.find_element_by_id("mousehover")
#
# action.move_to_element(menu).perform()
#
# submenu = driver.find_element_by_link_text("Top")
#
# action.move_to_element(submenu).click().perform()


# To right click on a button - action.context_click(driver.find_element).perform()

# To perform double click on a button - action.double_click(driver.find_element).perform()
