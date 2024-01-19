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

@pytest.mark.api
def test_repo_can_be_found(github_api):
     r = github_api.search_repo("become-qa-auto")
     assert r["total_count"] == 54  # counts how many "become-qa-auto" repos are there
     assert "become-qa-auto" in r["items"] [0] ["name"]  # verifies that first repo contains "become-qa-auto"
    

@pytest.mark.api
def test_repo_cannot_be_found(github_api):  # verifies that "sergiibutenko_repo_non_exist" repo is not present
    r = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert r["total_count"] == 0


@pytest.mark.api  
def test_repo_with_single_char_can_be_found(github_api): #  verifies that there is a repo with name that contains only 1 symbol
    r = github_api.search_repo("s")
    assert r["total_count"] != 0
