# Solution to the AJAX Form Submit Intermediate Challenge

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils import helpers, constants

def main():
    
    # Initialize Firefox Driver without the GUI
    fox_driver = helpers.get_firefox_driver("-headless")
    
    # Make an HTTP GET Request to the AJAX Form Webpage
    fox_driver.get(constants.AJAX_FORM_SUBMIT_DEMO)
    
    print("Filling Up AJAX Form: ")
    
    # Fill up the AJAX form and get server response
    server_response = fill_up_ajax_form(fox_driver, "Edward Johnson", "My name is Edward Johnson." \
        + "\nI come from Canada and I love snowboarding.")
    
    print("Server Response: \n" + server_response) 
    
    fox_driver.close()
    

def fill_up_ajax_form(driver, name_value, comment_value):
    """Fill up and submit an AJAX Form."""
    
    # Grab Required DOM elements
    name_input_field = driver.find_element(By.ID, "title")
    description_text_area = driver.find_element(By.ID, "description")
    submit_btn = driver.find_element(By.CSS_SELECTOR, "input[value='submit']")
    
    # Send text to the input field
    name_input_field.send_keys(name_value)
    
    # Clear the text area before entering text to it
    description_text_area.clear()
    
    # Send description to text area
    description_text_area.send_keys(comment_value)
    
    # Click the Submit button to begin AJAX HTTP POST Request
    submit_btn.click()
    
    # Create a wait object to wait for certain events
    wait = WebDriverWait(driver, 10)
    
    # Wait for the response div to appear
    div_response = wait.until(EC.visibility_of_element_located((By.ID, "submit-control")))
    
    # Get loading response
    loading_response = div_response.text
    res = "\nLoading Response: " + loading_response
    
    # Now wait for the text of this div to change to the success response
    wait.until(text_changed(driver, div_response))
    
    # Now Grab the new text
    success_response = div_response.text
    res += "\nSuccess Response: " + success_response
    
    return res


def text_changed(driver, element):
    """Check for a change of text in a given element."""
    
    def inner(driver):
        
        current_text = element.text
        
        return current_text != inner.last_text
    
    inner.last_text = element.text
    
    return inner    
    
if __name__ == "__main__":
    main()