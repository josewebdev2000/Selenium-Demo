# Solution to Table Search Challenge
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
import csv

from utils import constants, helpers

from time import sleep

def main():
    
    fox_driver = helpers.get_firefox_driver()
    fox_driver.get(constants.TABLE_DATA_SEARCH_DEMO)
    
    try:
        
        first_table = fox_driver.find_element(By.ID, "task-table")
        first_input_table = fox_driver.find_element(By.ID, "task-table-filter")
        second_table = fox_driver.find_element(By.CSS_SELECTOR, "table:not([id='task-table'])")
        
        # Get tasks from first table that are in progress
        first_table_data = get_data_from_words(first_table, first_input_table, "in progress")
        
        # Grab all people whose first name starts with B from the second table
        second_table_data = get_data_from_columns(fox_driver, second_table, "first name", "B")
        
        # Save data from first row in CSV file
        store_data_in_csv_file(first_table_data, "in-progress-tasks.csv")
        
        # Save data from second row in CSV file
        store_data_in_csv_file(second_table_data, "names-that-start-with-B.csv")
        
        # Display data from first table in the console
        print("Tasks in progress: \n")
        display_table_data(first_table_data)
        
        # Display data from second table in the console
        print("Names that start with B: \n")
        display_table_data(second_table_data)
        
    
    except Exception as e:
        raise e
    
    finally:
        sleep(3)
        fox_driver.close()


def get_data_from_words(table_element, input_element, keyword):
    """Return a 2D array representing the rows of data a table shows according to a keyword."""
    
    # Initialize the 2D array to represents rows of data
    data_rows = []
    
    # Clear out the input element by default
    input_element.clear()
    
    # Add headers to the rows of data
    headers = get_table_headers(table_element)  
    data_rows.append(headers)
    
    # Enter keyword to the input element
    input_element.send_keys(keyword)
    
    # Grab the table rows that do not have a style property of display none
    body_container = table_element.find_element(By.TAG_NAME, "tbody")
    row_elements = body_container.find_elements(By.CSS_SELECTOR, "tr:not([style*='display: none'])")
    
    for row_element in row_elements:
        
        row_data = []
        nested_columns = row_element.find_elements(By.TAG_NAME, "td")
        
        for nested_column in nested_columns:
            
            row_data.append(nested_column.text)
        
        data_rows.append(row_data)
    
    return data_rows

def get_data_from_columns(driver, table_element, column_name, keyword):
    """Create a 2D array of representing rows of data shown after entering a keyword to a column."""
    
    # Define acceptbale column names
    acceptable_column_names = ("#", "username", "first name", "last name")
    
    # If the column name does not belong, throw an error
    if column_name.lower() not in acceptable_column_names:
        raise ValueError(f"{column_name} is not a valid column name.")
    
    # Define the rows of data
    data_rows = []
    
    # Grab the headers
    headers = get_table_headers(table_element, "second")
    data_rows.append(headers)
    
    # Enter the keyword to the input element
    input_elements= table_element.find_elements(By.CSS_SELECTOR, "tr.filters > th > input")
    proper_input = list(filter(lambda ie: ie.get_attribute("placeholder") == column_name.title(), input_elements))[0]
    
    # Try to send keys to input element
    try:
        proper_input.send_keys(keyword)
    
    except ElementNotInteractableException:
        
        filter_btn = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-default.btn-xs.btn-filter")
        filter_btn.click()
        proper_input.send_keys(keyword)
    
    # Grab rows of data displayed
    body_container = table_element.find_element(By.TAG_NAME, "tbody")
    row_elements = body_container.find_elements(By.CSS_SELECTOR, "tr:not([style*='display: none'])")
    
    for row_element in row_elements:
        
        row_data = []
        nested_columns = row_element.find_elements(By.TAG_NAME, "td")
        
        for nested_column in nested_columns:
            
            row_data.append(nested_column.text)
        
        data_rows.append(row_data)
    
    return data_rows
    
def get_table_headers(table_element, table="first"):
    """Get the table headers from a table."""
    
    headers_container = table_element.find_element(By.TAG_NAME, "thead")
    
    # Add headers to the rows of data
    if table.lower() == "first":
        headers_elements = headers_container.find_elements(By.CSS_SELECTOR, "tr > th")
        
        headers = [header_element.text for header_element in headers_elements]
        
        return headers
    
    else:
        header_elements = headers_container.find_elements(By.CSS_SELECTOR, "tr.filters > th > input")
        
        headers = []
        
        for header_element in header_elements:
            
            input_placeholder = header_element.get_attribute("placeholder")
            headers.append(input_placeholder)
        
        return headers

def display_table_data(table_data):
    """Display table data to STDOUT"""
    
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