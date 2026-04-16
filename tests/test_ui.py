from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


BASE_URL = "http://127.0.0.1:8000/static/index.html"


def setup_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )


def test_products_click():
    driver = setup_driver()
    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 10)

    nav_items = wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "nav-item"))
    )

    nav_items[1].click()

    # ✅ Check active page instead of text
    active_page = driver.find_element(By.CSS_SELECTOR, ".page.active")

    assert "page-products" in active_page.get_attribute("id")

    driver.quit()


def test_alerts_click():
    driver = setup_driver()
    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 10)

    nav_items = wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "nav-item"))
    )

    nav_items[2].click()

    active_page = driver.find_element(By.CSS_SELECTOR, ".page.active")

    assert "page-alerts" in active_page.get_attribute("id")

    driver.quit()


def test_report_click():
    driver = setup_driver()
    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 10)

    nav_items = wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "nav-item"))
    )

    nav_items[3].click()

    active_page = driver.find_element(By.CSS_SELECTOR, ".page.active")

    assert "page-report" in active_page.get_attribute("id")

    driver.quit()