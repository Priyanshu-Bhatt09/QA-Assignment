from selenium import webdriver
from selenium.webdriver.common.by import By ## Tells Selenium how to find elements on the page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait ##this creates a timer


BASE_URL = "https://www.saucedemo.com"
PASSWORD = "secret_sauce"
TIMEOUT = 15


def create_driver():
    options = webdriver.ChromeOptions() ## it creates chrome settings
    options.add_argument("--start-maximized") ##opens chrome in full screen
    return webdriver.Chrome(options=options)


def login(driver, username, password=PASSWORD):
    wait = WebDriverWait(driver, TIMEOUT) ##create a 15 sec wait
    driver.get(BASE_URL)
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

## first test
def test_valid_login():
    driver = create_driver() ## opens chrome and creates a driver object
    try:
        login(driver, "standard_user")
        wait = WebDriverWait(driver, TIMEOUT)
        inventory_title = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        )
        assert inventory_title.text == "Products" ##if the title is not "Products" the test will fail
    finally:
        driver.quit() ## always close the browser even if the login fails

## second test
def test_add_item_to_cart_and_checkout():
    driver = create_driver()
    try:
        wait = WebDriverWait(driver, TIMEOUT)
        login(driver, "standard_user")

        wait.until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        ).click() ##find add to cart button and click it
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click() ##find the cart icon and click it

        cart_item = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "cart_item")) ## gets the cart item
        )
        assert "Sauce Labs Backpack" in cart_item.text

        driver.find_element(By.ID, "checkout").click() ##clicks checkout

        wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys(
            "Test"
        )
        driver.find_element(By.ID, "last-name").send_keys("User")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_info")))
        driver.find_element(By.ID, "Finish").click() ## finish button

        complete_header = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
        )
        assert "Thank you" in complete_header.text ##waits until it gets success message
    finally:
        driver.quit()

## third test
def test_locked_out_user_error_message():
    driver = create_driver()
    try:
        login(driver, "locked_out_user")
        wait = WebDriverWait(driver, TIMEOUT)
        error_box = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
        )
        assert "locked out" in error_box.text.lower() ##check if the error message contains "locked out"
    finally:
        driver.quit()

