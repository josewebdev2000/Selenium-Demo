# Solution to JavaScript Alert Exercise

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils import helpers, constants

def main():
    
     # Make a Firefox Driver but do not open the GUI
    fox_driver = helpers.get_firefox_driver("-headless")
    
    # Make an HTTP GET request to the desired website
    fox_driver.get(constants.JS_ALERTS_DEMO)
    
    alert_response = alert_box_exercise(fox_driver)
    print("JS Alert Exercise: ")
    print(alert_response)
    
    confirm_response = confirm_box_exercise(fox_driver, False)
    print("\nJS Confirm Alert Exercise: ")
    print(confirm_response)
    
    prompt_response = prompt_box_exercise(fox_driver, "Jose Brache Garcia")
    print("\nJS Prompt Exercise: ")
    print(prompt_response)
    
    fox_driver.close()

def alert_box_exercise(driver):
    """Click a button, get an alert and read its message."""
    
    # Grab required DOM Elements
    btn = driver.find_element(By.CSS_SELECTOR, "button[onclick='myAlertFunction()']")
    
    # Scroll down to the button to click
    driver.execute_script(constants.SCROLL_DOWN_JS_SCRIPT, btn)
    
    # Click the button
    btn.click()
    
    # Get the alert
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    
    # Get alert message
    alert_message = alert.text
    
    # Accept alert
    alert.accept()
    
    # Return alert message
    return alert_message  

def confirm_box_exercise(driver, accept=True):
    """Click a button, interact with confirm box, and read result."""
    
    # Grab required DOM elements
    btn = driver.find_element(By.CSS_SELECTOR, "button[onclick='myConfirmFunction()']")
    p_response = driver.find_element(By.ID, "confirm-demo")
    
    # Scroll down to the button to click
    driver.execute_script(constants.SCROLL_DOWN_JS_SCRIPT, btn)
    
    # Click the button
    btn.click()
    
    # Grab the confirmation popup message
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    
    # Consider whether or not to accept the alert
    if accept:
        alert.accept()
    
    else:
        alert.dismiss()
    
    # Return the message found in the p tag
    return p_response.text  

def prompt_box_exercise(driver, name):
    """Click a button, enter some data and get website's response."""
    
    # Grab required DOM elements
    btn = driver.find_element(By.CSS_SELECTOR, "button[onclick='myPromptFunction()']")
    p_response = driver.find_element(By.ID, "prompt-demo")
    
    # Click the button
    btn.click()
    
    # Grab the prompt alert
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    
    # Enter the name of the user
    alert.send_keys(name)
    
    # Accept the alert
    alert.accept()
    
    # Return the response from the p tag
    return p_response.text

if __name__ == "__main__":
    main()