from selenium import webdriver
from selenium.webdriver.common.by import By

import allure

@allure.step('step1: click Home page Overlapped Element link')
def OverlappedElement_page(driver):
    page = driver.find_element(By.XPATH, "//a[@href='/overlapped']")
    page.click()
    assert page,f"can't find Overlapped Element link"

@allure.step('step2: scroll element into view')
def scroll_page(driver,name):
    scroll = driver.execute_script("arguments[0].scrollIntoView()", name)
    assert f"can't scroll into view"

@allure.step('step3: entering text into the Name input field')
def input_text(name):
    name.click()
    name.send_keys("test")
    assert name,f"text entered uncorrectly"


@allure.title('Overlapped Element')
@allure.description('Make element visible to enter text')
def test_LoadDelay_function():
    driver = webdriver.Chrome()   # chromedriver
    driver.get('http://uitestingplayground.com/') 
    OverlappedElement_page(driver)
    name = driver.find_element(By.XPATH, "//input[@id='name']")
    scroll_page(driver,name)
    input_text(name)