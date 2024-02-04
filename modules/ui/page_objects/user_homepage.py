from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserHomepage(BasePage):
    URL = "https://github.com/login"

    def __init__(self) -> None:
        super().__init__()   

    # open "https://github.com/login" page
    def go_to(self):
        self.driver.get(UserHomepage.URL)

    # sing in into user profile
    def login(self, username, password):
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
    
    def click_user_menu_button(self):

        # find user profile button in the top right cornet
        btn_user = self.driver.find_element(By.XPATH, '//button[@aria-label="Open user account menu"]')

        # click user menu btn
        btn_user.click()

    def check_username(self):
        user_name_text = self.driver.find_element(By.XPATH, "//span[contains(text(), 'QAtester7')]")
        return user_name_text.text.strip() # retrives text of the element
    
    
    def click_x_user_menu(self):
        # find X btn at user menu pane and wait for 5 sec before click
        get_close_user_menu = self.driver.find_element(By.XPATH, "//header/div[1]/div[2]/div[3]/deferred-side-panel[1]/include-fragment[1]/user-drawer-side-panel[1]/dialog-helper[1]/dialog[1]/div[1]/div[1]/div[2]/button[1]/*[1]")
        close_user_menu = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(get_close_user_menu))

        # click on X to close user menu
        close_user_menu.click()


