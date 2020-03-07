from Locators.Locator import Locator

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = Locator.username_textbox_id
        self.password_textbox_id = Locator.password_textbox_id
        self.login_button_id = Locator.login_button_id

    def username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def login(self):
        self.driver.find_element_by_id(self.login_button_id).click()
