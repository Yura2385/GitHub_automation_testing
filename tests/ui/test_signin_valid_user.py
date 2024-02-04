from modules.ui.page_objects.sign_in_page import SignInPage
import pytest
import time


@pytest.mark.ui   
def test_log_in_with_valid_credentials():
     # create page object
    sign_in_page = SignInPage()

     # open "https://github.com/login" page
    sign_in_page.go_to()

     # sing in into user profile
    sign_in_page.try_login("mtester.round@gmail.com", "Im_testing_007")
    #time.sleep(2)
    
     # verift page title
    assert sign_in_page.check_title("GitHub")

     # Close browser
    sign_in_page.close()
