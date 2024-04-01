from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
import allure
import random
import string

@allure.testcase('Click')
def test_Click():
    driver = webdriver.Chrome()   # 指向 chromedriver 的位置
    driver.get('http://uitestingplayground.com/') 

    button = driver.find_element(By.XPATH, "//a[@href='/click']")
    button.click()

    test_button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
    test_button.click()

    try:
        test_button = driver.find_element(By.XPATH, "//button[@class='btn btn-success']")
        assert True
    except:
        assert False