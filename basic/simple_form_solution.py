# Solution to the Simple Form Basic Exercise

from selenium.webdriver.common.by import By

from utils import helpers
from utils import constants

def main():
    
    # Make a firefox driver and do not open a browser window
    my_fox_driver = helpers.get_firefox_driver("-headless")
    
    # Make a GET HTTP request to the desired website
    my_fox_driver.get(constants.SIMPLE_FORM_URL)
    
    message_to_send_single_input = "I am the best"
    
    # Practice entering input and getting result data
    single_output = enter_message_input_field(my_fox_driver, message_to_send_single_input)
    
    
    m1 = "3"
    m2 = "7"
    
    # Practice entering data to two input fields
    out_2 = enter_message_two_input_fields(my_fox_driver, m1, m2)
    
    # Show results to the console
    print(f"Result from sending \"{message_to_send_single_input}\" to the simple form: {single_output}")
    print(f"Result from sending {m1} and {m2} to the addition form: {out_2}")
    
    
    # Close the browser
    my_fox_driver.close()

def enter_message_input_field(driver, message):
    """Enter a message in an input field and return result."""
    
    # Get input element with a CSS selector
    single_input = driver.find_element(By.CSS_SELECTOR, "input#user-message")
    
    # Send the message to the input as keystrokes
    single_input.send_keys(message)
    
    # Grab the submit button appropiate to the grabbed input element
    single_btn = driver.find_element(By.CSS_SELECTOR, "form#get-input > button.btn.btn-primary")
    
    # Click the button to send data
    single_btn.click()
    
    # return the result
    return driver.find_element(By.ID, "display").text

def enter_message_two_input_fields(driver, m1, m2):
    """Practice sending two messages.""" 
    
    # Grab input boxes by their IDs
    input_1 = driver.find_element(By.ID, "value1")
    input_2 = driver.find_element(By.ID, "value2")
    
    # Enter corresponding messages to corresponding input elements
    input_1.send_keys(m1)
    input_2.send_keys(m2)
    
    # Grab the button that submits the data
    submit_btn = driver.find_element(By.CSS_SELECTOR, "form#gettotal > button.btn.btn-primary")
    
    # Click the button
    submit_btn.click()
    
    # return the result to the user
    return driver.find_element(By.ID, "displayvalue").text

if __name__ == "__main__":
    main()