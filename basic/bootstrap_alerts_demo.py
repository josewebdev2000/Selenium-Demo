# Solution for Bootstrap Alert Messages

from selenium.webdriver.common.by import By

from utils import helpers, constants

def main():
    
    # Make a tuple of dictionaries with the CSS selectors of the buttons and divs of each Bootstrap alert
    btns_n_divs_selectors = (
        
        {
            "button_selector": "button#autoclosable-btn-success",
            "div_selector": "div.alert-autocloseable-success"
        },
        {
            "button_selector": "button#normal-btn-success",
            "div_selector": "div.alert-normal-success"
        },
        {
            "button_selector": "button#autoclosable-btn-warning",
            "div_selector": "div.alert-autocloseable-warning"
        },
        {
            "button_selector": "button#normal-btn-warning",
            "div_selector": "div.alert-normal-warning"
        },
        {
            "button_selector": "button#autoclosable-btn-danger",
            "div_selector": "div.alert-autocloseable-danger"
        },
        {
            "button_selector": "button#normal-btn-danger",
            "div_selector": "div.alert-normal-danger"
        },
        {
            "button_selector": "button#autoclosable-btn-info",
            "div_selector": "div.alert-autocloseable-info"
        },
        {
            "button_selector": "button#normal-btn-info",
            "div_selector": "div.alert-normal-info"
        }
    )
    
    # Make a Firefox Driver but do not open the GUI
    fox_driver = helpers.get_firefox_driver("-headless")
    
    # Make an HTTP GET request to the required webpage
    fox_driver.get(constants.BOOTSTRAP_ALERTS_DEMO)
    
    #Loop through every single button and div alert
    for btn_n_div_selector in btns_n_divs_selectors:
        
        alert_response = alert_bootstrap_exercise(fox_driver, 
                                                  btn_n_div_selector["button_selector"], 
                                                  btn_n_div_selector["div_selector"])
        
        print(alert_response)
    
    fox_driver.close()

def alert_bootstrap_exercise(driver, btn_css_selector, alert_css_selector):
    """Click a Button that Opens Up a Bootstrap Alert"""
    
    # Grab required DOM Elements
    btn = driver.find_element(By.CSS_SELECTOR, btn_css_selector)
    alert_div = driver.find_element(By.CSS_SELECTOR, alert_css_selector)
    
    # Get button child for alert div if any
    btn_div_child = get_button_child_from_div(driver, alert_div)
    
    # Click the button to fire up the Bootrap Button
    btn.click()
    
    # Grab the response
    response = alert_div.text
    
    # Close the div if required
    if btn_div_child:
        btn_div_child.click()
    
    return response

def get_button_child_from_div(driver, div_web_element):
    """Return the button that's a child of the given div."""
    
    children = div_web_element.find_elements(By.CSS_SELECTOR, "*")
    
    for child in children:
        if child.tag_name == "button":
            return child
    
    return None
    

if __name__ == "__main__":
    main()