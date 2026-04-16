from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def test_dashboard_loads():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("http://127.0.0.1:8000/static/index.html")

    time.sleep(2)

    # Check title
    assert "Inventory Dashboard" in driver.title

    driver.quit()


def test_products_button():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("http://127.0.0.1:8000/static/index.html")

    time.sleep(2)

    button = driver.find_element(By.XPATH, "//button[contains(text(),'Products')]")
    button.click()

    time.sleep(2)

    assert "Products" in driver.page_source

    driver.quit()