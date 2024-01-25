from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By  


class SignInPage(BasePage):
    URL = "https://github.com/login"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # Find input field - Username or email address to type in invalid user credentials
        login_elem = self.driver.find_element(By.ID, "login_field")

        # Enter invalid user credentials
        login_elem.send_keys(username)

        # Find input field - Password to type in invalid user credentials
        pass_elem = self.driver.find_element(By.ID, "password")

        # Enter invalid password
        pass_elem.send_keys(password)

        # Find Sign In button
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # Click Sign In btn
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
    