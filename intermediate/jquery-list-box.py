# Solution to the jQuery List Box Challenge
from selenium.webdriver.common.by import By

from utils import constants, helpers

from time import sleep

def main():
    
    fox_driver = helpers.get_firefox_driver()
    fox_driver.get(constants.JQUERY_LIST_BOX_DEMO)
    
    try:
        # Grab common DOM elements that will be used throghout the whole script
        add_select = fox_driver.find_element(By.CLASS_NAME, "pickData")
        remove_select = fox_driver.find_element(By.CLASS_NAME, "pickListResult")
        add_button = fox_driver.find_element(By.CLASS_NAME, "pAdd")
        add_all_button = fox_driver.find_element(By.CLASS_NAME, "pAddAll")
        remove_button = fox_driver.find_element(By.CLASS_NAME, "pRemove")
        remove_all_button = fox_driver.find_element(By.CLASS_NAME, "pRemoveAll")
        
        # Add/remove elements as required
        add_one_element(add_select, add_button, "Helena")
        remove_one_element(remove_select, remove_button, "Helena")
        add_all_elements(add_all_button)
        remove_multiple_elements(remove_select, remove_button, "Isabella", "Manuela", "Laura",
                                 "Luiza", "Valentina", "Beatriz", "Lara", "Julia", "Sophia")
        add_multiple_elements(add_select, add_button, "Isabella", "Manuela", "Julia", "Beatriz",
                              "Valentina", "Sophia")
        remove_all_elements(remove_all_button)   
         
    except Exception as e:
        raise e
    
    finally:
        sleep(3)
        fox_driver.close()
        
def add_one_element(addSelect, addBtn, optionName):
    
    # Get options available at the add select element right now
    available_options = addSelect.find_elements(By.TAG_NAME, "option")
    
    # Grab the required option
    required_option = list(filter(lambda option: option.text == optionName, available_options))[0]
    
    # Click that option
    required_option.click()
    
    # Click the add button
    addBtn.click()

def remove_one_element(removeSelect, removeBtn, optionName):
    
    # Get options available at the add select element right now
    available_options = removeSelect.find_elements(By.TAG_NAME, "option")
    
    # Grab the required option
    required_option = list(filter(lambda option: option.text == optionName, available_options))[0]
    
    # Click that option
    required_option.click()
    
    # Click the remove button
    removeBtn.click()

def add_multiple_elements(addSelect, addBtn, *optionNames):
    
    # Get options available at the add select element right now
    available_options = addSelect.find_elements(By.TAG_NAME, "option")
    
    # Create a list to store the required options to add
    required_options = list(filter(lambda option: option.text in optionNames, available_options))
    
    # Click every option
    for required_option in required_options:
        required_option.click()
    
    # Click the add button
    addBtn.click()

def remove_multiple_elements(removeSelect, removeBtn, *optionNames):
    
    # Get options available at the remove select element right now
    available_options = removeSelect.find_elements(By.TAG_NAME, "option")
    
    # Create a list to store the required options to remove
    required_options = list(filter(lambda option: option.text in optionNames, available_options))
    
    # Click every option
    for required_option in required_options:
        required_option.click()
    
    # Click the remove button
    removeBtn.click()
        
def add_all_elements(addAllBtn):
    
    # Click the button to add all elements
    addAllBtn.click()

def remove_all_elements(removeAllBtn):
    
    # Click the button to remove all elements
    removeAllBtn.click()
    
if __name__ == "__main__":
    main()