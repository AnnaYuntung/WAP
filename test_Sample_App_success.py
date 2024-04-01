from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest
import allure
import random
import string


@allure.title('Sample App login fail with wrong password')
@allure.description('check App can login success')
def test_SampleApp_function_success():
    driver = webdriver.Chrome()   # chromedrive
    driver.get('http://uitestingplayground.com/') 
    SampleApp_page(driver)
    characters = string.ascii_letters + string.digits
    generated_string = ''.join(random.choice(characters))

    user_name = driver.find_element(By.XPATH, "//input[@name='UserName']")
    password = driver.find_element(By.XPATH, "//input[@name='Password']")
    login_button = driver.find_element(By.XPATH, "//button[@id='login']")
    input_correct(user_name,password,generated_string)
    success(driver,login_button)


@allure.step('step1: click Home page Sample App link')
def SampleApp_page(driver):
    page = driver.find_element(By.XPATH, "//a[@href='/sampleapp']")
    page.click()
    assert page,f"can't find Sample App link"

def input_correct(user_name,password,generated_string):   
    user_name.click()
    user_name.send_keys(generated_string)
        
    password.click()
    password.send_keys("pwd")

    assert user_name, f"username entered uncorrectly"
    assert password, f"password entered uncorrectly"

def success(driver,login_button):
    login_button.click()
    login_status = driver.find_element(By.CLASS_NAME, 'text-success')
    logout_button = driver.find_element(By.XPATH, "//button[text()='Log Out']")

    assert login_status, f"Not find success text"
    assert logout_button, f"Not find logout button"
 
@allure.step('step4: click Log Out button and check logged out') 
def log_out(driver,login_button):
    login_button.click()
    login_status = driver.find_element(By.CLASS_NAME, 'text-info')

    assert login_status, f"Not find Log Out text"





