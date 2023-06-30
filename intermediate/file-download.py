# Solution to File Download Exercise
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

"""
TO SOLVE THIS CHALLENGE WELL. IN THE read_file FUNCTION CHECK ALL FILES THAT
CONTAIN THE easyinfo STRING IN THEIR NAMES, THEN GET THE ONE WITH THE HIGHEST
NUMBER TO GET THE LATEST FILE AVAILABLE.

Delete all other files that start with easyinfo
"""

import os
from utils import constants
import re

# This case requires us to set up the Selenium Firefox Driver By Ourselves

from time import sleep

def main():
    
    download_dir = os.getenv("DOWNLOAD_DIR")
    fox_driver = generate_firefox_driver(download_dir)
    fox_driver.get(constants.FILE_DOWNLOAD_DEMO)
    
    try:
        
        # Define text to enter
        some_txt = get_user_input()
        
        # Grab unchanging text area element
        text_area = fox_driver.find_element(By.ID, "textbox")
        
        download_file(fox_driver, text_area, some_txt)
        latest_filename = handle_downloaded_file(download_dir)
        file_txt = read_file(latest_filename)
        
        print("\nInformation found in downloaded file: \n")
        print(file_txt)
    
    except Exception as e:
        raise e
    
    finally:
        sleep(3)
        fox_driver.close()
    

def generate_firefox_driver(download_dir):
    """Generate and return the Firefox Driver required for this challenge."""
    
    # Initialize an Options and a Service Object
    fox_service = Service(constants.DRIVER_PATH)
    fox_options = Options()
    
    fox_options.set_preference("browser.download.folderList", 2)
    fox_options.set_preference("browser.download.dir", download_dir)
    fox_options.set_preference("browser.download.manager.showWhenStarting", False)
    fox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,text/plain")
    
    # Enter required options
    #fox_options.add_argument('-headless')
    
    return webdriver.Firefox(service = fox_service, options = fox_options)
      

def download_file(driver, text_area, text):
    """Download a file from the web and save it wherever the user wants."""
    
    # Clear text area by default
    text_area.clear()
    
    # Send keys to text area with text to enter
    text_area.send_keys(text)
    
    # Create a wait object to wait for buttons to be clickeable or visible
    wait = WebDriverWait(driver, 10)
    
    # Grab button to generate text file (Wait for it to be clickeable)
    generate_btn = wait.until(EC.element_to_be_clickable((By.ID, "create")))
    
    # Click the button
    generate_btn.click()
    
    # Grab the a link to download the generated file
    download_link = wait.until(EC.element_to_be_clickable((By.ID, "link-to-download")))
    
    # Click the link
    download_link.click()

def handle_downloaded_file(folder_container_path):
    """Return the appropiate file name of the file to read"""
    
    # Get a list of all text files that start with easyinfo
    def is_right_file(file_name):
        return file_name.startswith("easyinfo") and file_name.endswith(".txt")
    
    # Find file that has the greatest number on it 
    def find_latest_file(file_names):
        
        latest_file = ""
        
        if len(file_names) > 1:
    
            nums = []
            
            for file_name in file_names:
            
                # Find a number in the file name
                match_num_obj = re.search(r"\d+", file_name)
                
                if match_num_obj:
                    num = int(match_num_obj.group())
                else:
                    num = 0
                
                nums.append(num)
            
            greatest_num = max(nums)
            latest_file = list(filter(lambda file_name : str(greatest_num) in file_name ,file_names))[0]
        
        else:
            latest_file = file_names[0]
        
        return latest_file
    
    right_files = list(filter(is_right_file, os.listdir(folder_container_path)))
    filename_to_return = find_latest_file(right_files)
    return filename_to_return   
    

def get_user_input():
    """Let the user enter what they want to then download the file."""
    
    num_lines = int(input("Enter the number of lines to enter: "))
    
    print("You have a limit of 500 characters.")
    
    lines = [input("Enter a line of text here: ") for i in range(num_lines)]
    
    return "\n".join(lines)

def read_file(filename):
    """Get the information found in the downloaded file"""
    
    with open(filename, "r") as f:
        return f.read()
    
def get_substring(ori_str, char_limit):
    """ Return a string according to a character limit."""
    
    return ori_str[:char_limit] if char_limit <= len(ori_str) else ori_str

if __name__ == "__main__":
    main()
