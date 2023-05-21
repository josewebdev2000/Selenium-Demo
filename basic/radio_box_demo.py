# Solution to the Radio Box Exercise

from selenium.webdriver.common.by import By

from utils import helpers
from utils import constants

def main():
    
    # Get firefox driver with headless option on
    my_fox_driver = helpers.get_firefox_driver("-headless")
    
    # Make an HTTP GET request to the radio buttons website
    my_fox_driver.get(constants.RADIO_BOX_DEMO)
    
    # Chose genders on the first exercise
    male_message = gender_exercise(my_fox_driver, 'male')
    female_message = gender_exercise(my_fox_driver, 'female')
    
    print("Results From First Radio Button Exercises: \n")
    print(f"Choosing Male Gender Message: {male_message}")
    print(f"Choosing Female Gender Message: {female_message}")

    # Chose genders on the second exercise
    boy_toddler = gender_n_age_exercise(my_fox_driver, "male", "0-5")
    teenage_girl = gender_n_age_exercise(my_fox_driver, "female", "5-15")
    dad = gender_n_age_exercise(my_fox_driver, "male", "15-50")
    mom = gender_n_age_exercise(my_fox_driver, "female", "15-50")
    
    print("\nResults From Second Radio Button Exercises: \n")
    print(f"Results for toddler: {boy_toddler}")
    print(f"Results for teenager: {teenage_girl}")
    print(f"Results for adult 1: {dad}")
    print(f"Results for adult 2: {mom}")


def gender_exercise(driver, chosen_gender):
    """Return Gender user response message"""
    
    # Get relevant DOM elements
    radio_to_find = None
    button_check = driver.find_element(By.ID, "buttoncheck")
    p_response = driver.find_element(By.CSS_SELECTOR, "p.radiobutton")
    
    # Get the chosen radio button according to user choice
    if chosen_gender.capitalize() == "Male":
        
        radio_to_find= driver.find_element(By.CSS_SELECTOR, 'input[type="radio"][name="optradio"][value="Male"]')
    
    elif chosen_gender.capitalize() == "Female":
        
        radio_to_find = driver.find_element(By.CSS_SELECTOR, 'input[type="radio"][name="optradio"][value="Female"]')
    else:
        return "Invalid Option"
    
    # Click the chosen button
    radio_to_find.click()
    
    # Click button to get message
    button_check.click()
    
    # return the text in the response paragraph
    return p_response.text

def gender_n_age_exercise(driver, chosen_gender, chosen_age_group):
    """Return gender and age use response message."""
    
    # Grab required DOM elements
    radio_gender = None
    radio_age_group = None
    btn_response_getter = driver.find_element(By.CSS_SELECTOR, "button[onclick='getValues();']")
    p_response = driver.find_element(By.CLASS_NAME, "groupradiobutton")
    
    # Grab appropriate gender
    if chosen_gender.capitalize() == "Male":
        radio_gender = driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='Male'][name='gender']")
    
    elif chosen_gender.capitalize() == "Female":
        radio_gender = driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='Female'][name='gender']")
    
    else:
        return "Invalid Option"
    
    # Grab appropriate age group
    if chosen_age_group == "0-5":
        radio_age_group = driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='0 - 5'][name='ageGroup']")
    
    elif chosen_age_group == "5-15":
        radio_age_group = driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='5 - 15'][name='ageGroup']")
    
    elif chosen_age_group == "15-50":
        radio_age_group = driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='15 - 50'][name='ageGroup']")
    
    else:
        return "Invalid Option"
    
    # Click the chosen options
    radio_gender.click()
    radio_age_group.click()
    
    # Click the button to get response message
    btn_response_getter.click()
    
    # Return the response
    return p_response.text

if __name__ == "__main__":
    main()