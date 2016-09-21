from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('c:/temp/chromedriver.exe')
driver.get(sys.argv[1])

elem = driver.find_element_by_id("LoginUsername")
elem.send_keys("K34686")

elem = driver.find_element_by_id("LoginPassword")
elem.send_keys("Vintaf0")

elem = driver.find_element_by_id("loginBtn").click()

driver.switch_to_frame("ext-gen73")

elem = driver.find_element_by_id("X24")
elem.clear()
elem.send_keys("K34686")

driver.switch_to_default_content()

elem = driver.find_element_by_id("ext-gen266").click()

actions = ActionChains(driver)
actions.send_keys(Keys.LEFT_ALT + Keys.F12) #approve btn
actions.perform()

driver.close()
driver.quit()
