# Solution to Select Element Exercise

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from utils import helpers, constants

def main():
    
    fox_driver = helpers.get_firefox_driver("-headless")
    
    fox_driver.get(constants.SELECT_DROPDOWN_DEMO)
    
    print("First Dropdown Exercises: \n")
    
    weekday = dropdown_select_exercise(fox_driver, "monday")
    weekend = dropdown_select_exercise(fox_driver, "saturday")
    
    print(f"The weekday selected is: {weekday}")
    print(f"The weekend selected is: {weekend}")
    
    # Do the second exercise
    print("\nSecond Dropdown Exercise: \n")
    
    one_state = multi_select_exercise(fox_driver, "New Jersey")
    two_states = multi_select_exercise(fox_driver, "Texas")
    
    print(one_state)
    print(two_states)
    
    fox_driver.close()

def dropdown_select_exercise(driver, day):
    """Select a day and return the result of doing so."""
    
    # Grab DOM elements of interest
    select_dropdown = driver.find_element(By.ID, "select-demo")
    p_response = driver.find_element(By.CLASS_NAME, "selected-value")
    
    # Create a Select Object to be able to select
    select_obj = Select(select_dropdown)
    
    # Select day by value attribute of HTML element
    select_obj.select_by_value(day.capitalize())
    
    # Return the text from p tag
    return p_response.text

def multi_select_exercise(driver, state):
    """Select an element from a dropdown and return the response."""
    
    # Grab DOM elements of interest
    select_dropdown = driver.find_element(By.ID, "multi-select")
    btn_first = driver.find_element(By.ID, "printAll")
    p_response = driver.find_element(By.CLASS_NAME, "getall-selected")
    option_to_choose = driver.find_element(By.CSS_SELECTOR, f"select#multi-select > option[value='{state}']")
    
    # Create action chains
    actions = ActionChains(driver)
    
    # Scroll to the dropdown element
    driver.execute_script(constants.SCROLL_DOWN_JS_SCRIPT, select_dropdown)
    
    # Press Ctrl down
    actions.key_down(Keys.CONTROL)
    
    # Go to select element
    actions.move_to_element(select_dropdown)
    
    # Scroll to the option to choose
    driver.execute_script(constants.SCROLL_DOWN_JS_SCRIPT, option_to_choose)
    
    # Move to the desired option
    actions.move_to_element(option_to_choose)
    
    # Click on the selected option
    actions.click()
    
    # Release the Ctrl Key
    actions.key_up(Keys.CONTROL)
    
    # Perfom actions
    actions.perform()
    
    # Create actions for button
    btn_actions = ActionChains(driver)
    
    # Scroll to the button element
    driver.execute_script(constants.SCROLL_DOWN_JS_SCRIPT, btn_first)
    
    btn_actions.click(btn_first)
    
    btn_actions.perform()
    
    return p_response.text
    

if __name__ == "__main__":
    main()