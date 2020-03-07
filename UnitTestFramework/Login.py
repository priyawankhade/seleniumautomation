from selenium import webdriver
import time
import unittest

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/priya/PycharmProject/newproject/Driver/ChromeDriver/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        time.sleep(10)

        self.driver.find_element_by_id("txtUsername").send_keys("admin")
        time.sleep(10)

        self.driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys('admin123')
        time.sleep(20)

        self.driver.find_element_by_name("Submit").click()

        time.sleep(10)

        self.driver.find_element_by_id("welcome").click()

        time.sleep(10)

        self.driver.find_element_by_link_text("Logout").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

        cls.driver.quit()

        print('Test Passed and Logout Successful ! ')






