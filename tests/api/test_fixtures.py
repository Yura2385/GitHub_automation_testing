import pytest

# fixtures are the functions that can be run before the actual test

@pytest.mark.check
def test_change_name(user):
    assert user.name == "Yuriy"

@pytest.mark.check
def test_change_second_name(user):
    assert user.second_name == "Zhyvko"
   
