from selenium import webdriver
import unittest
from Locators.Pages.HomePage import HomePage
from Locators.Pages.LoginPage import LoginPage

class LocatorTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/priya/ChromeDriver/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.username("Admin")
        login.password("admin123")
        login.login()

        home_page = HomePage(driver)
        home_page.welcome()
        home_page.logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test Passed and Logout Successful ! ')