# import pytest
# import yaml
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
#
# with open("testdata.yaml") as f:
#     testdata = yaml.safe_load(f)
#     browser = testdata["browser"]
#
# @pytest.fixture(scope="session")
# def browser():
#     if browser == "firefox":
#         service = Service(executable_path=GeckoDriverManager().install())
#         options = webdriver.FirefoxOptions()
#         driver = webdriver.Firefox(service=service, options=options)
#     else:
#         service = Service(executable_path=ChromeDriverManager().install())
#         options = webdriver.ChromeOptions()
#         driver = webdriver.Chrome(service=service, options=options)
#     yield driver
#     driver.quit()
import pytest

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open('testdata.yaml') as f:
    test_data = yaml.safe_load(f)
    browser = test_data['browser']


@pytest.fixture(scope='session')
def browser():
    if browser == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def title():
    return 'Sea'
@pytest.fixture()
def description():
    return 'Mountains'
@pytest.fixture()
def content():
    return 'The mountains are wonderful'

@pytest.fixture()
def your_name():
    return 'Irina'
@pytest.fixture()
def your_email():
    return 'Irina@gmail.com'
@pytest.fixture()
def your_content():
    return 'Cats are funny'