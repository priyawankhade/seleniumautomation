from Locators.Locator import Locator

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.welcome_link_id = Locator.welcome_link_id
        self.logOut_link_text = Locator.logOut_link_text

    def welcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def logout(self):
        self.driver.find_element_by_link_text(self.logOut_link_text).click()
