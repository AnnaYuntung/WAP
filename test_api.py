import requests
from requests import get

import allure

@allure.title('success requests')
@allure.description('check Facts')
def test_success():
    param = {'animal_type': 'cat', 'amount': '1'}
    url = 'https://cat-fact.herokuapp.com/facts/animal_type=cat&amount=1'

    response = requests.get(url, params=param)

    print(response.content)
    print(response.status_code)
    assert response.content, response.status_code

@allure.title('change animal_type')
@allure.description('change animal_type, it should retern error status_code')
def test_fail():
    param = {'animal_type': 'horse', 'amount': '1'}
    url = 'https://cat-fact.herokuapp.com/facts/animal_type=cat&amount=1'

    response = requests.get(url, params=param)

    assert response.content, response.status_code
    print(response.status_code)

@allure.title('change amount')
@allure.description('change amount, it should retern error status_code')
def test_fail_1():
    param = {'animal_type': 'cat', 'amount': '0'}
    url = 'https://cat-fact.herokuapp.com/facts/animal_type=cat&amount=1'

    response = requests.get(url, params=param)

    assert response.content, response.status_code
    print(response.status_code)

