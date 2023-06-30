# Solution to Table Pagination Challenge
from selenium.webdriver.common.by import By

from utils import helpers, constants

from time import sleep

import csv

def main():
    
    # Get the driver
    fox_driver = helpers.get_firefox_driver()
    
    # Go to required webpage
    fox_driver.get(constants.TABLE_PAGINATION_DEMO)
    
    try:
        # Grab DOM elements that will be always used
        table = fox_driver.find_element(By.TAG_NAME, "table")
        nav_links_container = fox_driver.find_element(By.ID, "myPager")
        nav_links = nav_links_container.find_elements(By.TAG_NAME, "li")
        
        nums = [3, 2, 1]
        
        for num in nums:
            
            click_nav_link(nav_links, num)
            table_data = get_table_data(table)
            display_table_data(table_data)
            store_data_in_csv_file(table_data, f"data_file{num}.csv")
    
    except Exception as e:
        raise e
    
    finally:
        sleep(3)
        fox_driver.close()

def click_nav_link(nav_links, btn_num):
    """Click a navigation button."""
    
    # Grab the required nav link
    required_nav_link = None
    
    for nav_link in nav_links:
        
        nested_link = nav_link.find_element(By.TAG_NAME, "a")
        
        if str(btn_num) == nested_link.text:
            required_nav_link = nested_link
            break
    
    # Click the nav link
    if required_nav_link != None:
        required_nav_link.click()

def get_table_data(table_to_read):
    """Get table data from the table to read."""
    
    # Store all data from the table here
    # This will be a 2D list
    table_data = []
    
    # Grab headers first
    table_header = table_to_read.find_element(By.TAG_NAME, "thead")
    headers = table_header.find_elements(By.CSS_SELECTOR, "tr > th")
    
    headers_txt = []
    
    for header in headers:
        
        headers_txt.append(header.text)
    
    table_data.append(headers_txt)
    
    # Grab body data
    table_body = table_to_read.find_element(By.TAG_NAME, "tbody")
    shown_rows = table_body.find_elements(By.CSS_SELECTOR, "tr[style='display: table-row;']")
    
    for shown_row in shown_rows:
        
        # Grab td data
        nested_td_tags = shown_row.find_elements(By.TAG_NAME, "td")
        
        row_data = []
        
        for nested_td_tag in nested_td_tags:
            
            row_data.append(nested_td_tag.text)
        
        table_data.append(row_data)
    
    return table_data

def display_table_data(table_data):
    """Display table data to STDOUT"""
    
    print("\nData Received: \n")
    for row in table_data:
        
        text_to_print = " ".join(row)
        print(text_to_print)


def store_data_in_csv_file(table_data, csv_filename):
    """Store received table data in CSV file"""
    
    # Define headers and data
    headers = table_data[0]
    data = table_data[1:]
    
    # Write the CSV file
    with open(csv_filename, "w") as csv_file:
        
        csv_writer = csv.writer(csv_file)
        
        # Write headers
        csv_writer.writerow(headers)
        
        # Write data
        csv_writer.writerows(data)         

if __name__ == "__main__":
    main()