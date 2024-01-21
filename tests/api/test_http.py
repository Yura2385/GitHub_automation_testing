import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(r.text)
    
@pytest.mark.http # - here we have two oprions to verify the values and just print them.
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers

    assert body['name'] == 'Chris Wanstrath' # - verifies if this key-value pair: 'name': 'Chris Wanstrath' present in the body
    # print(f"Response Body is {r.json()}") # - just prints entire body 
    assert r.status_code == 200
    # print(f"Response Status code is {r.status_code}") # - just prints the status code 
    assert headers['Server'] == 'GitHub.com'
    # print(f"Response Headers are {r.headers}") # - just prints the headers


@pytest.mark.http 
def test_status_request():
    r = requests.get('https://api.github.com/users/sergii_butenko')

    assert r.status_code == 404
    








