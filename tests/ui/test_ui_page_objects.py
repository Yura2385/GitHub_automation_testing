from modules.ui.page_objects.sign_in_page import SignInPage
import pytest
import time


@pytest.mark.ui   
def test_check_incorect_username_page_object():
     # create page object
    sign_in_page = SignInPage()

     # open "https://github.com/login" page
    sign_in_page.go_to()

     # trying to sing in
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

     # verift page title
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")
    #time.sleep(2)

     # Close browser
    sign_in_page.close()
