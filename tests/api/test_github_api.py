import pytest


 #  test #1
@pytest.mark.api     
def test_user_exists(github_api):  # verifies that user exists 
    user = github_api.get_user("defunkt")  # get the user
    assert user["login"] == "defunkt"


 #  test #2
@pytest.mark.api     
def test_user_not_exists(github_api):  # verifies that user doesn't exist
    r = github_api.get_user("butenkosergii")
    #  print(r) - we need to run it only first time to find out what message we get when user is not registred, and then use it later for assert
    assert r["message"] == "Not Found"


 #  test #3
@pytest.mark.api
def test_repo_can_be_found(github_api):
     r = github_api.search_repo("become-qa-auto")
     assert r["total_count"] == 54  # counts how many "become-qa-auto" repos are there
     assert "become-qa-auto" in r["items"] [0] ["name"]  # verifies that first repo contains "become-qa-auto"
    

 #  test #4
@pytest.mark.api
def test_repo_cannot_be_found(github_api):  # verifies that "sergiibutenko_repo_non_exist" repo is not present
    r = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert r["total_count"] == 0


 #  test #5
@pytest.mark.api  
def test_repo_with_single_char_can_be_found(github_api): #  verifies that there is a repo with name that contains only 1 symbol
    r = github_api.search_repo("s")
    assert r["total_count"] != 0


 #  test #6
@pytest.mark.api  
def test_verify_particular_emojis(github_api): #  verifies that listed emijis are present
    r = github_api.get_emoji()
    assert all(value in r for value in ["+1", "zzz", "100", "wood", "wink", "v", "-1"])

 #  test #7
@pytest.mark.api  
def test_verify_particular_emoji_not_exists(github_api): #  verifies that listed emiji not present
    r = github_api.get_emoji()
    assert r != "pryvit"
    

 #  test #8
@pytest.mark.api 
def test_verify_status_code(github_api):
    r = github_api.get_body_of_commits_list("octocat", "Hello-World")
    #print(r)
    #body = r.json()
    #headers = r.headers
    assert r.status_code == 200


#  test #9
@pytest.mark.api 
def test_verify_sha(github_api):
    r = github_api.get_body_of_commits_list("octocat", "Hello-World")
    #print(r)
    body = r.json() #  converts response JSON (body) into a Python list
    assert body[0]["sha"] == "7fd1a60b01f91b314f59955a4e4d4e80d8edf11d"


#  test #10
@pytest.mark.api 
def test_verify_status_not_found_non_existing_user(github_api):
    r = github_api.get_commits_list("octoca12", "Hello-World")
    #print(r)
    assert r.status_code == 404


