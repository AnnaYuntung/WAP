from selenium import webdriver
from selenium.webdriver.common.by import By

import allure
import random
import string

# def test_SampleApp():
#     SampleApp_function_success()
#     SampleApp_function_fail_with_correct_password()
#     SampleApp_function_fail_with_wrong_password()

@allure.step('step1: click Home page Sample App link')
def SampleApp_page(driver):
    page = driver.find_element(By.XPATH, "//a[@href='/sampleapp']")
    page.click()
    assert page,f"can't find Sample App link"

@allure.step('step2: input any non-empty username and correct password')
def input_correct(username,password,generated_string):   
    username.click()
    username.send_keys(generated_string)
        
    password.click()
    password.send_keys("pwd")

    assert username, f"username entered uncorrectly"
    assert password, f"password entered uncorrectly"
        
@allure.step('step3: click Log In button and check login success') 
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


@allure.step('step2: input empty username and correct password')
def input_empty_username(username,password):   
    username.click()
    username.send_keys("")

    password.click()
    password.send_keys("pwd")

    assert username, f"username entered uncorrectly"
    assert password, f"password entered uncorrectly"
        
@allure.step('step3: click Log In button and check login fail') 
def fail(driver,login_button):
    login_button.click()
    login_status = driver.find_element(By.CLASS_NAME, 'text-danger')

    assert login_status, f"Not find Invalid username/password text"


@allure.step('step2: input any non-empty username and wrong password')
def input_wrong_password(username,password,generated_string):   
    username.click()
    username.send_keys(generated_string)

    password.click()
    password.send_keys(generated_string)

    assert username, f"username entered uncorrectly"
    assert password, f"password entered uncorrectly"

@allure.title('login success')
@allure.description('check App can login')
def test_SampleApp_function_success():
    driver = webdriver.Chrome()   # chromedrive
    driver.get('http://uitestingplayground.com/') 
    characters = string.ascii_letters + string.digits
    generated_string = ''.join(random.choice(characters))
    SampleApp_page(driver)
    username = driver.find_element(By.XPATH, "//input[@name='UserName']")
    password = driver.find_element(By.XPATH, "//input[@name='Password']")
    login_button = driver.find_element(By.ID, 'login')
    input_correct(username,password,generated_string)
    success(driver,login_button)

@allure.title('login fail with correct password')
@allure.description('check App can login fail')
def test_SampleApp_function_fail_with_correct_password():
    driver = webdriver.Chrome()   # chromedrive
    driver.get('http://uitestingplayground.com/') 
    SampleApp_page(driver)
    username = driver.find_element(By.XPATH, "//input[@name='UserName']")
    password = driver.find_element(By.XPATH, "//input[@name='Password']")
    login_button = driver.find_element(By.ID, 'login')
    input_empty_username(username,password)
    fail(driver,login_button)

@allure.title('login fail with wrong password')
@allure.description('check App can login fail')
def test_SampleApp_function_fail_with_wrong_password():
    driver = webdriver.Chrome()   # chromedrive
    driver.get('http://uitestingplayground.com/') 
    characters = string.ascii_letters + string.digits
    generated_string = ''.join(random.choice(characters))
    SampleApp_page(driver)
    username = driver.find_element(By.XPATH, "//input[@name='UserName']")
    password = driver.find_element(By.XPATH, "//input[@name='Password']")
    login_button = driver.find_element(By.ID, 'login')
    input_wrong_password(username,password,generated_string)
    fail(driver,login_button)


