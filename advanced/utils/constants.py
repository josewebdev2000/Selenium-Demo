# Global constants from simple page URL
from os import getenv

# Environment variables (Default value for Ubuntu Distros)
DRIVER_PATH = getenv("DRIVER_PATH", "/usr/local/bin")
BIN_PATH = getenv("BIN_PATH", "/usr/bin/firefox")

# Links 
TABLE_PAGINATION_DEMO = "https://demo.seleniumeasy.com/table-pagination-demo.html"


# JS Scripts
SCROLL_DOWN_JS_SCRIPT = "arguments[0].scrollIntoView();"