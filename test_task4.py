import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Ie()
    request.addfinalizer(wd.quit)
    return wd

def test_task4(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    WebDriverWait(driver,10).until(EC.title_is("My Store"))
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()       