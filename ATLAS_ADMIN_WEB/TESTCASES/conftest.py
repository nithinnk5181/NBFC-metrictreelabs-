from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='Chrome':
        driver = webdriver.Chrome(executable_path="RESOURCES/chromedriver")
        driver.maximize_window()
        #driver.execute_script("document.body.style.zoom='80%'")
        #driver.find_element(By.TAG_NAME, value='html').send_keys(Keys.CONTROL, '-')
        #action = ActionChains(driver)
        #action.key_down(Keys.CONTROL).send_keys('-').key_up(Keys.CONTROL).perform()
        #action.key_down(Keys.CONTROL).send_keys('-').key_up(Keys.CONTROL).perform()
        driver.implicitly_wait(60)
        #driver.set_window_position(0, 1)
        print("Launching Chromebrowser")
        return driver


    elif browser=='Firefox':
        driver = webdriver.Firefox(executable_path="RESOURCES/chromedriver")
        driver.implicitly_wait(60)
        driver.set_window_position(0, 1)
        print("Launching Firefoxbrowser")
        return driver



def pytest_addoption(parser):   #This will get the alue from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  #This will return the browser value to setup method
    return request.config.getoption("--browser")

