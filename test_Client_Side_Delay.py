from selenium import webdriver
from selenium.webdriver.common.by import By

import allure


@allure.step('step1: click Home page Client Side Delay link')
def ClientSideDelay_page(driver):
    page = driver.find_element(By.XPATH, "//a[@href='/clientdelay']")
    page.click()
    assert page,f"can't find Client Side Delay link"

@allure.step('step2: click button')
def load_page(driver):
    button = driver.find_element(By.XPATH, "//button[@id='ajaxButton']")
    button.click()
    driver.implicitly_wait(15)

@allure.testcase('step3: check test can wait for element to show up')
def load_success(driver):
    success_txet = driver.find_element(By.XPATH, "//p[@class='bg-success']")
    assert success_txet,f"can't find success text"

@allure.title('Client Side Delay')
@allure.description('Some elements may appear after client-side time consuming JavaScript calculations')
def test_ClientSideDelay_function():
    driver = webdriver.Chrome()   # chromedriver
    driver.get('http://uitestingplayground.com/') 
    ClientSideDelay_page(driver)
    load_page(driver)