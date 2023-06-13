# Global constants from simple page URL
from os import getenv

# Environment variables (Default value for Ubuntu Distros)
DRIVER_PATH = getenv("DRIVER_PATH", "/usr/local/bin")
BIN_PATH = getenv("BIN_PATH", "/usr/bin/firefox")

# Links 
SIMPLE_FORM_URL = "https://demo.seleniumeasy.com/basic-first-form-demo.html"
CHECK_BOX_DEMO = "https://demo.seleniumeasy.com/basic-checkbox-demo.html"
RADIO_BOX_DEMO = "https://demo.seleniumeasy.com/basic-radiobutton-demo.html"
SELECT_DROPDOWN_DEMO = "https://demo.seleniumeasy.com/basic-select-dropdown-demo.html"
JS_ALERTS_DEMO = "https://demo.seleniumeasy.com/javascript-alert-box-demo.html"

# JS Scripts
SCROLL_DOWN_JS_SCRIPT = "arguments[0].scrollIntoView();"