# Solution to Progress Bar Modal Exercise

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils import helpers, constants

from time import sleep

def main():
    
    fox_driver = helpers.get_firefox_driver()
    fox_driver.get(constants.PROGRESS_BAR_MODAL_DEMO)
    wait = WebDriverWait(fox_driver, 10)
    
    try:
        first_modal_text = show_dialog(wait,"button.btn.btn-primary")
        second_modal_text = show_dialog(wait, "button.btn.btn-success")
        third_modal_text = show_dialog(wait, "button.btn.btn-warning")
        
        print("First Modal Text: ")
        print(first_modal_text)
        
        print("\nSecond Modal Text: ")
        print(second_modal_text)
        
        print("\nThird Modal Text: ")
        print(third_modal_text)
    
    except Exception as e:
        raise e
    
    finally:
        sleep(3)
        fox_driver.close()


def show_dialog(wait_obj, btn_css_selector):
    """Show the first autocloseable dialog."""
    
    # Gather CSS Selectors of important elements in tuples
    button_css_selector_tuple = (By.CSS_SELECTOR, btn_css_selector)
    modal_css_selector_tuple = (By.CSS_SELECTOR, "div.modal")
    
    # Wait for the button to open this button to be clickeable
    first_dialog_btn = wait_obj.until(EC.element_to_be_clickable(button_css_selector_tuple))
    first_dialog_btn.click()
    
    # Grab the modal that just appeared
    shown_modal = wait_obj.until(EC.visibility_of_element_located(modal_css_selector_tuple))
    
    # Grab the text of the modal
    modal_text = shown_modal.text
    
    # Wait for modal to become invisible again
    wait_obj.until(EC.invisibility_of_element(modal_css_selector_tuple))
    
    # Return the text displayed by the modal
    return modal_text
    

if __name__ == "__main__":
    main()