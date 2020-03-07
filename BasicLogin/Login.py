from selenium import webdriver

import time

driver = webdriver.Chrome(executable_path="/Users/priya/ChromeDriver/chromedriver")
driver.get("https://opensource-demo.orangehrmlive.com/")

time.sleep(5)

driver.find_element_by_id("txtUsername").send_keys("admin")
time.sleep(5)

driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys('admin123')
time.sleep(5)


driver.find_element_by_name("Submit").click()

time.sleep(5)

driver.find_element_by_id("welcome").click()

time.sleep(5)

driver.find_element_by_link_text("Logout").click()

print('Test Passed and Logout Successful ! ')

driver.close()

driver.quit()