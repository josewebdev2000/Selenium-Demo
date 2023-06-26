# Global constants from simple page URL
from os import getenv

# Environment variables (Default value for Ubuntu Distros)
DRIVER_PATH = getenv("DRIVER_PATH", "/usr/local/bin")
BIN_PATH = getenv("BIN_PATH", "/usr/bin/firefox")

# Links 
INPUT_FORM_WITH_VALIDATION_DEMO="https://demo.seleniumeasy.com/input-form-demo.html"
AJAX_FORM_SUBMIT_DEMO = "https://demo.seleniumeasy.com/ajax-form-submit-demo.html"
JQUERY_SELECT_DROPDOWN_DEMO = "https://demo.seleniumeasy.com/jquery-dropdown-search-demo.html"

# JS Scripts
SCROLL_DOWN_JS_SCRIPT = "arguments[0].scrollIntoView();"