# Solution to Bootstrap List Box Exercise
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils import helpers, constants

from time import sleep

def main():
    
    # Initialize Firefox Driver and show the Browser GUI
    fox_driver = helpers.get_firefox_driver()
    
    # Make an HTTP GET Request to the webpage of interest
    fox_driver.get(constants.BOOTSTRAP_LIST_BOX_DEMO)
    
    # Try to successfully execute
    try:
        move_from_one_point_to_another(fox_driver, "left", "bootstrap-duallist", "Dapibus ac facilisis in")
        move_from_one_point_to_another(fox_driver, "right", "Cras justo odio", "Porta ac consectetur ac")
    
    except Exception as e:
        raise e
    
    finally:
        sleep(3)
        fox_driver.close()


def move_from_one_point_to_another(driver, direction_of_origin, *chosen_options):
    """Grab elements from the left/right and move them to the right/left."""
    
    # Define key variables to grab required DOM elements
    position_of_ul = direction_of_origin
    move_btn = "right" if direction_of_origin == "left" else "left"
    
    wait = WebDriverWait(driver, 10)
    
    # Grab DOM elements of interest
    options_ul_css_selector = (By.CSS_SELECTOR, f"div.dual-list.list-{position_of_ul}.col-md-5 ul")
    move_btn_css_selector = (By.CSS_SELECTOR, f"span.glyphicon.glyphicon-chevron-{move_btn}")
    
    left_options_ul = wait.until(EC.presence_of_element_located(options_ul_css_selector)) 
    move_btn = wait.until(EC.element_to_be_clickable(move_btn_css_selector))
    
    # Grab all li elements found
    all_options = left_options_ul.find_elements(By.TAG_NAME, "li")
    
    # Deactivate all active li's to avoid unexpected behaviour
    for li in all_options:
        
        if "active" in li.get_attribute("class"):
            li.click()
    
    
    # Choose which li elements will be moved
    option_criteria = lambda li : li.text in chosen_options
    chosen_li = list(filter(option_criteria, all_options))
    
    # Click every single chosen li to focus them
    for li in chosen_li:
        li.click()
        
    # Move the chosen li to the right
    move_btn.click()
    
    

if __name__ == "__main__":
    main()