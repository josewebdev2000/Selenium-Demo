# Generic functions that help to solve exercises
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

import utils.constants as constants

def get_firefox_driver(*args):
    """Return a Firefox driver for automation project."""
    
    # Set up Firefox Options
    firefox_options = Options()
    
    # Enter as many arguments as the user has specified
    for arg in args:
        firefox_options.add_argument(arg)
    
    # Create a new Firefox driver service
    firefox_service = Service(constants.DRIVER_PATH)
    
    # Create the firefox driver
    firefox_driver = webdriver.Firefox(service=firefox_service,
                                       options=firefox_options)
    
    # return the driver
    return firefox_driver
    
    