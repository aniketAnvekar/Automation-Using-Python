import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.rahulshettyacademy.com/angularpractice/')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
