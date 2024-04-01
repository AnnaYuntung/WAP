from selenium import webdriver
from selenium.webdriver.common.by import By

import allure

@allure.step('step1: click Home page Load Delay link')
def Scrollbars_page(driver):
    page = driver.find_element(By.XPATH, "//a[@href='/scrollbars']")
    page.click()
    assert page,f"can't find Scrollbars link"

@allure.step('step2: scroll element into view')
def scroll_page(driver, button):
    scroll_bar = driver.execute_script("arguments[0].scrollIntoView()", button)
    assert f"can't scroll into view"

@allure.step('step3: click button')
def click_button(button):
    button.click()
    assert button, f"can't find button"

@allure.title('Scrollbars')
@allure.description('Scrolling an element into view may be a tricky task')
def test_Scrollbars_function():
    driver = webdriver.Chrome()   # chromedriver
    driver.get('http://uitestingplayground.com/') ,
    Scrollbars_page(driver)
    button = driver.find_element(By.XPATH, "//button[@id='hidingButton']")
    scroll_page(driver, button)
    click_button(button)

    
