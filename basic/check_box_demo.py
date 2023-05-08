# Solution to the Check Box Demo Exercise
import random

from selenium.webdriver.common.by import By

from utils import helpers
from utils import constants

def main():
    # Make a firefox driver and do not open a browser window
    my_fox_driver = helpers.get_firefox_driver("-headless")
    
    # Make a GET HTTP request to the desired website
    my_fox_driver.get(constants.CHECK_BOX_DEMO)
    
    success_output = check_success_checkbox(my_fox_driver)
        
    result_all_True = multiple_checkboxes(my_fox_driver, True)
    result_all_False = multiple_checkboxes(my_fox_driver, False)
    
    print(f"Result from checking success check box: {success_output}")
    print(f"Result from checking all checkboxes: {result_all_True}")
    print(f"Result from checking some checkboxes: {result_all_False}")
    
    # Close the browser
    my_fox_driver.close()

def check_success_checkbox(driver):
    """Return message from clicking success checkbox."""
    
    # Get success HTML input element by ID
    success_input = driver.find_element(By.ID, "isAgeSelected")
    
    # Click it
    success_input.click()
    
    # Return message from clicking it
    return driver.find_element(By.ID, "txtAge").text

def multiple_checkboxes(driver, check_all=True):
    """Return message from checking all boxes or only some."""
    
    # Grab super parent_div 
    super_parent_div = driver.find_element(By.CSS_SELECTOR, ".col-md-6.text-left")
    
    # Grab next parent divs
    next_parent_divs = super_parent_div.find_elements(By.CSS_SELECTOR, ".panel.panel-default")
    next_parent_divs.pop(0)
    
    # Move to next parent div
    closer_parent_div = next_parent_divs[0].find_element(By.CSS_SELECTOR, ".panel-body")
    
    # Grab all checkbox parents
    checkbox_parents = closer_parent_div.find_elements(By.CSS_SELECTOR, ".checkbox")
    
    checkboxes = []
    
    # Grab each checkbox found on each checkbox_parent
    for checkbox_parent in checkbox_parents:
        checkbox = checkbox_parent.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
        checkboxes.append(checkbox)
    
    # Grab input of type button to grab button that checks all checkboxes
    checkboxes_checker = closer_parent_div.find_element(By.CSS_SELECTOR, "input[type='button']")
    
    if check_all:
        checkboxes_checker.click()
    
    else:
        random_num = random.randint(1, len(checkboxes))
        
        random_checkboxes = random.sample(checkboxes, random_num)
        
        for box in random_checkboxes:
            box.click()
    
    return checkboxes_checker.get_attribute("value")
    

if __name__ == "__main__":
    main()
