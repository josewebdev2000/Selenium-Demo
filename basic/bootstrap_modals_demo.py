from selenium.webdriver.common.by import By

from utils import helpers, constants

# WAIT FOR MODAL BUTTONS TO BE CLICKABLE BEFORE USING THEM
def main():
    
    # Initialize a Firefox Driver without the GUI
    fox_driver = helpers.get_firefox_driver("-headless")
    
    # Make an HTTP GET request to the required webpage
    fox_driver.get(constants.BOOTSTRAP_MODALS_DEMO)
    
    print("Single Modal Exercise: \n")
    
    single_response = single_modal_exercise(fox_driver)
    print(single_response)
    
    print("\nModal Inside Modal Exercise: ")
    
    # Refresh the page
    fox_driver.refresh()
    
    nested_response = nested_modal_exercise(fox_driver)
    
    print(nested_response)
    
    fox_driver.close()

def single_modal_exercise(driver):
    """Display a Bootstrap Modal and then cancel it out."""
    
    # Grab required DOM Elements
    btn = driver.find_element(By.CSS_SELECTOR, "a[href='#myModal0']")
    
    # Click the button
    btn.click()
    
    # Wait for the modal to appear and grab it
    modal = driver.find_element(By.ID, "myModal0")
    
    modal_message = modal.text
    # Close the modal
    
    btn_close = modal.find_element(By.CLASS_NAME, "close")
    
    btn_close.click()
    
    return modal_message

def nested_modal_exercise(driver):
    """Display a modal that displays another."""
    
    # Grab required DOM elements
    btn = driver.find_element(By.CSS_SELECTOR, "a[href='#myModal']")
    
    # Click the button
    btn.click()
    
    modals_text = ""
    
    # Grab the first modal
    first_modal = driver.find_element(By.ID, "myModal")
    
    # Add first modal text to text of modals
    modals_text += "First Modal Text: \n\n"
    modals_text += first_modal.text
    
    # Grab button to fire up second modal
    btn_second = driver.find_element(By.CSS_SELECTOR, "a[href='#myModal2']")
    
    # Click the button to fire up second modal
    btn_second.click()
    
    # Grab the second modal
    second_modal = driver.find_element(By.ID, "myModal2")
    
    # Concatenate text of the second modal
    modals_text += "\nSecond Modal Text: \n\n"
    modals_text += second_modal.text
    
    return modals_text

if __name__ == "__main__":
    main()