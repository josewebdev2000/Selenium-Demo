# Solution to jQuery Select Dropdown
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from utils import helpers, constants

from time import sleep

def main():
    
    # Initialize the Firefox Driver with the Browser GUI
    fox_driver = helpers.get_firefox_driver()
    
    # Make an HTTP GET request to the desired URL
    fox_driver.get(constants.JQUERY_SELECT_DROPDOWN_DEMO)
    
    try:
        
        print("jQuery Select Dropdown: ")
        single_select_exercise(fox_driver, "New Zealand")
        multiple_select_exercise(fox_driver, "Florida", "California", "New York", "New Jersey")
        single_select_with_disabled_options_exercise(fox_driver, "American Samoa", "Puerto Rico")
        select_with_category(fox_driver, "Java")
    
    except Exception as e:
        raise e
    
    finally:
        sleep(3)
    
        fox_driver.quit()

def single_select_exercise(driver, chosen_option):
    """Select a single option from the jQuery Select Dropdown."""
    
    # Grab the select element to grab the chosen option
    wait = WebDriverWait(driver, 10)
    
    select_css_selector = (By.CSS_SELECTOR, "select#country")
    
    # Wait for the select element to appear on the page
    select_dropdown = wait.until(EC.presence_of_element_located(select_css_selector))
    
    # Get the options from the select element
    options = select_dropdown.find_elements(By.TAG_NAME, "option")
    
    # Get the option that has the same value as the chosen option
    option_to_choose = list(filter(lambda option : option.get_attribute("value") == chosen_option.title(), options))[0].text
    
    # Grab the span element to click to open up jQuery Dropdown
    span_css_selector = (By.CSS_SELECTOR, "span[role='combobox'][aria-haspopup='true'][aria-labelledby='select2-country-container'][tabindex='0']")
    span_to_click = wait.until(EC.visibility_of_element_located(span_css_selector))
    
    # Click the span
    span_to_click.click()
    
    # Grab the input box to enter as text the option to choose
    input_css_selector = (By.CSS_SELECTOR, "span.select2-search.select2-search--dropdown > input.select2-search__field[type='search'][tabindex='0'][role='textbox']")
    input_to_enter_option = wait.until(EC.visibility_of_element_located(input_css_selector))
    
    # Send option to choose as keys
    input_to_enter_option.send_keys(option_to_choose)
    
    # Click the li of the ul list available to properly select the element
    li_css_selector = (By.CSS_SELECTOR, "ul#select2-country-results.select2-results__options[role='tree'] > li.select2-results__option.select2-results__option--highlighted[role='treeitem']")
    li_to_click = wait.until(EC.visibility_of_element_located(li_css_selector))
    li_to_click.click()

def multiple_select_exercise(driver, *chosen_options):
    """Select multiply options from a jQuery Select Dropdown."""
    
    # Create a wait object
    wait = WebDriverWait(driver, 10)
    
    # Select input element to enter text in it
    input_css_selector = (By.CSS_SELECTOR, "input[placeholder='Select state(s)']")
    input_to_get_text = wait.until(EC.element_to_be_clickable(input_css_selector))
    
    # Define CSS Selector for UL with options to select
    ul_options_css_selector = (By.CSS_SELECTOR, "ul.select2-results__options[role='tree'][aria-multiselectable='true'][aria-expanded='true'][aria-hidden='false']")
    
    # Define CSS Selector for highlighted li
    highlighted_li_css_selector = (By.CSS_SELECTOR, "li.select2-results__option.select2-results__option--highlighted")
    
    # Loop through the list of options
    for chosen_option in chosen_options:
        
        # Click the input to type text on it
        input_to_get_text.click()
        
        # Get the ul that contains options (wait for it to be visible)
        ul_options_holder = wait.until(EC.visibility_of_element_located(ul_options_css_selector))
        
        # Send the option as keys to the input element
        input_to_get_text.send_keys(chosen_option)
        
        # Select the highlighted li from the ul (if any)
        highlighted_li = ul_options_holder.find_element(*highlighted_li_css_selector)
        highlighted_li.click()

def single_select_with_disabled_options_exercise(driver, title, chosen_option):
    """Select a single option from a jQuery dropdown that could be disabled."""
    
    # Initialize a wait object
    wait = WebDriverWait(driver, 10)
    
    # Grab the element required to start selecting options
    element_to_click_first_css_selector = (By.CSS_SELECTOR, f"span.select2-selection__rendered[title='{title}']")
    element_to_click_first = wait.until(EC.element_to_be_clickable(element_to_click_first_css_selector))
    
    # Click the element to get the input to write the option on it
    element_to_click_first.click()
    
    # Grab the input element to enter text there
    input_to_enter_text_css_selector = (By.CSS_SELECTOR, "input.select2-search__field:not([style])")
    input_to_enter_text = wait.until(EC.element_to_be_clickable(input_to_enter_text_css_selector))
    
    # Send chosen option to that input
    input_to_enter_text.send_keys(chosen_option)
    
    # Grab the ul that contains the option to choose
    ul_option_container_css_selector = (By.CSS_SELECTOR, "ul.select2-results__options[role='tree'][aria-expanded='true'][aria-hidden='false']")
    ul_option_container = wait.until(EC.visibility_of_element_located(ul_option_container_css_selector))
    
    # Grab the highlighted li
    highlighted_li_css_selector = (By.CSS_SELECTOR, "li.select2-results__option.select2-results__option--highlighted")
    
    try:
        highlighted_li = ul_option_container.find_element(*highlighted_li_css_selector)
    
    except:
        print("This option is disabled or does not exist.")
    
    else:
        # Click the highlighted li
        highlighted_li.click()
        
def select_with_category(driver, chosen_option):
    """Select an option given its category."""
    
    # Grab the required select element that contains categories and options
    select_html_element_css_selector = (By.CSS_SELECTOR, "select#files")
    select_html_element = driver.find_element(*select_html_element_css_selector)
    
    # Make a Select Object to select the desired option
    select_obj = Select(select_html_element)
    
    # Select by visible text
    select_obj.select_by_visible_text(chosen_option)
    
if __name__ == "__main__":
    main()