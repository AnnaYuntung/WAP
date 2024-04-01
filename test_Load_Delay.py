from selenium import webdriver
from selenium.webdriver.common.by import By

import allure



@allure.step('step1: click Home page Load Delay link')
def LoadDelay_page(driver):
    page = driver.find_element(By.XPATH, "//a[@href='/loaddelay']")
    page.click()
    assert page,f"can't find Load Delay link"

@allure.step('step2: page loaded and button is available')
def load_page(driver):
    get_url = driver.current_url
    driver.get(get_url)
    button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
    assert button, f"can't find button"

@allure.title('Load Delay')
@allure.description('Ensure that a test is capable of waiting for a page to load')
def test_LoadDelay_function():
    driver = webdriver.Chrome()   # chromedriver
    driver.get('http://uitestingplayground.com/') 
    LoadDelay_page(driver)
    load_page(driver)