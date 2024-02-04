import pytest  # import pytest module to mark tests

from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # module for searching objects by their attributes
import time

@pytest.mark.ui  
def test_check_incorrect_username():
     # Create an object to handle webbrowser 
    driver = webdriver.Chrome(service=Service (ChromeDriverManager().install()))

     # Open webpage: https://github.com/login
    driver.get("https://github.com/login")

     # Find input field - Username or email address to type in invalid user credentials
    login_elem = driver.find_element(By.ID, "login_field")

     # Enter invalid user credentials
    login_elem.send_keys("sergiibutenkomistakeinemail.com")
    # time.sleep(2)  # stops the execution for 2 sec
    
     # Find input field - Password to type in invalid user credentials
    pass_elem = driver.find_element(By.ID, "password")

     # Enter invalid password
    pass_elem.send_keys("wrong password")

     # Find Sign In button
    btn_elem = driver.find_element(By.NAME, "commit")

     # Click Sign In btn
    btn_elem.click()

     # Verify page title
    assert driver.title == "Sign in to GitHub · GitHub"
    
     # Close webbrowser
    driver.close()