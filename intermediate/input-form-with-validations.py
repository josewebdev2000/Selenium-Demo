# Solution to Intermediate Exercise Input Form with Validations
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from utils import constants, helpers

def main():
    
    # Initialize a Firefox Driver without showing the GUI
    fox_driver = helpers.get_firefox_driver("-headless")
    
    # Make an HTTP GET Request to the webpage of interest
    fox_driver.get(constants.INPUT_FORM_WITH_VALIDATION_DEMO)
    
    # Get a WebElement to the form of interest
    form_of_interest = get_form_element(fox_driver)
    
    # Send the first name
    given_fn = send_text_to_input(form_of_interest,
                                       "input[name='first_name']",
                                       "Gabriel")
    
    # Send the last name
    given_ln = send_text_to_input(form_of_interest,
                                  "input[name='last_name']",
                                  "Salazar")
    
    # Send the email
    given_email = send_text_to_input(form_of_interest,
                                     "input[name='email']",
                                     "gsalazar@examplemail.com")
    
    # Send a phone number
    given_pn = send_text_to_input(form_of_interest,
                                  "input[name='phone']",
                                  "1112223333")
    
    # Send an address
    given_address = send_text_to_input(form_of_interest,
                                       "input[name='address']",
                                       "804 Nowhere St")
    
    # Send a city
    given_city = send_text_to_input(form_of_interest,
                                    "input[name='city']",
                                    "Nowhere")
    
    # Select a state
    given_state = select_an_option(form_of_interest,
                                   "select[name='state']",
                                   "New Jersey")
    
    # Select Zip Code
    given_zip_code = send_text_to_input(form_of_interest,
                                        "input[name='zip']",
                                        "22222")
    
    # Select Website Domain
    given_web_domain = send_text_to_input(form_of_interest,
                                          "input[name='website']",
                                          "example.com")
    
    # Select hosting option
    given_hosting = check_radio_button(form_of_interest,
                                       "input[type='radio'][name='hosting'][value='no']")
    
    # Enter project description into textarea
    given_description = send_text_to_text_area(form_of_interest,
                                            "textarea[name='comment']",
                                            "This is just an example to practice automation with Selenium.")
    
    # Submit the form
    form_of_interest.submit()
    
    # Read form values
    print("\nFirst Name: " + given_fn)
    print("Last Name: " + given_ln)
    print("Email: " + given_email)
    print("Phone: " + given_pn)
    print("Address: " + given_address)
    print("City: " + given_city)
    print("State: " + given_state)
    print("ZIP Code: " + given_zip_code)
    print("Web Domain: " + given_web_domain)
    print("Hosting Available: " + given_hosting)
    print("Project Description: " + given_description + "\n")
    
def get_form_element(driver):
    """Return the form element of interest."""
    
    form = driver.find_element(By.ID, "contact_form")
    return form

def send_text_to_input(form_parent, input_css_selector, text_to_enter):
    """Send text to a certain input where text can be entered."""
    
    # Grab the input element of interest
    input_element = form_parent.find_element(By.CSS_SELECTOR, input_css_selector)
    
    # Send info to this input element
    input_element.send_keys(text_to_enter)
    
    # Return the value of this input after sending keys
    return input_element.get_attribute("value")

def send_text_to_text_area(form_parent, text_area_css_selector, text_to_enter):
    """Send text to a certain textarea element."""
    
    # Grab the text area element
    textarea_element = form_parent.find_element(By.CSS_SELECTOR, text_area_css_selector)
    
    # Clear out the text area
    textarea_element.clear()
    
    # Enter text to text area
    textarea_element.send_keys(text_to_enter)
    
    # Return text of textarea
    return textarea_element.get_attribute("value")

def select_an_option(form_parent, select_css_selector, option_displayed_text):
    """Select an option from a select element."""
    
    # Grab desired select element
    select_element = form_parent.find_element(By.CSS_SELECTOR, select_css_selector)
    
    # Create a Select Object in order to select an option
    select_obj = Select(select_element)
    
    # Get displayed texts of all options of this select element
    displayed_options_texts = [option.text for option in select_obj.options]
    
    # If option given is not an available option, make an early return
    if not option_displayed_text in displayed_options_texts:
        return "Could not select a valid option."
    
    # Select the option based on the text displayed
    select_obj.select_by_visible_text(option_displayed_text)
    
    # Return the text of the selected option
    selected_option = select_obj.first_selected_option
    
    return selected_option.text

def check_radio_button(form_parent, radio_btn_css_selector):
    """Check a radio button and."""
    
    # Grab radio button to select
    radio_btn = form_parent.find_element(By.CSS_SELECTOR, radio_btn_css_selector)
    
    # Check the radio button
    radio_btn.click()
    
    return radio_btn.get_attribute("value")

if __name__ == "__main__":
    main()