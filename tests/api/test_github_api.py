import pytest


@pytest.mark.api     
def test_user_exists(github_api):  # verifies that user exists 
    user = github_api.get_user("defunkt")  # get the user
    assert user["login"] == "defunkt"


@pytest.mark.api     
def test_user_not_exists(github_api):  # verifies that user doesn't exist
    r = github_api.get_user("butenkosergii")
    #  print(r) - we need to run it only first time to find out what message we get when user is not registred, and then use it later for assert
    assert r["message"] == "Not Found"


