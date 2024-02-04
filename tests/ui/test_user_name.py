from modules.ui.page_objects.user_homepage import UserHomepage
import pytest
import time


@pytest.mark.ui  
def test_username_under_user_menu():
     # create page object
    user_homepage = UserHomepage()
    
     # open "https://github.com/login" page
    user_homepage.go_to()

     # trying to sing in
    user_homepage.login("mtester.round@gmail.com", "Im_testing_007")

     # click user menu icon
    user_homepage.click_user_menu_button()
    time.sleep(0.2)

     # verify user name
    assert user_homepage.check_username() == "QAtester7"

     # close user menu
    user_homepage.click_x_user_menu()
    # time.sleep(2)