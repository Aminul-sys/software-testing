from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # STEP 1: Open the Signup Page
    print("Opening the Signup page...")
    driver.get("https://letcode.in/signup")

    # Initialize Explicit Wait
    wait = WebDriverWait(driver, 10)

    # Input data for testing
    full_name = "Muhammed Aminul"
    email = "muhammedaminul99@gmail.com"
    password = "SecurePass123!"

    # STEP 2: Locate Input Fields and Enter Data
    print("Entering data into the signup form...")

    # Locate and enter Full Name
    name_input = wait.until(EC.visibility_of_element_located((By.ID, "name")))
    name_input.send_keys(full_name)

    # Locate and enter Email
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys(email)

    # Locate and enter Password
    password_input = driver.find_element(By.ID, "pass")
    password_input.send_keys(password)

    # STEP 3: Submit the Signup Form
    print("Submitting the signup form...")
    signup_button = driver.find_element(By.XPATH, "//button[text()='SIGN UP']")
    signup_button.click()

    # STEP 4: Validate the Signup Result
    print("Validating the signup process...")
    success_message = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "notification"))
    ).text

    if "Account Created" in success_message:
        print("Signup was successful!")
    else:
        print(f"Signup failed: {success_message}")

except Exception as e:
    print(f"An error occurred during the test: {e}")

finally:
    # STEP 5: Close the Browser
    print("Closing the browser...")
    time.sleep(3)
    driver.quit()
