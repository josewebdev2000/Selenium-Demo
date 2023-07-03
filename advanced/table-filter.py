# Solution to Table Filter Challenge

from selenium.webdriver.common.by import By

from utils import constants, helpers

import csv

from time import sleep

# Make a 2D array to represent filter data with the following columns

# CHECKED, FAVOURITE, TYPE, TITLE, SUBTITLE, COLOR, DATE

# The previous represents all data that can be extracted from the table

def main():
    
    fox_driver = helpers.get_firefox_driver()
    fox_driver.get(constants.TABLE_FILTER_DEMO)
    
    try:
        
        table = fox_driver.find_element(By.CSS_SELECTOR, "table.table.table-filter")
        all_btn = fox_driver.find_element(By.CSS_SELECTOR, "button[data-target='all']")
        
        check_row_boxes(table, 2, 4)
        click_favourite_link(table, 1, 2, 3)
        
        button_pagados = fox_driver.find_element(By.CSS_SELECTOR, "button[data-target='pagado']")
        button_pendientes = fox_driver.find_element(By.CSS_SELECTOR, "button[data-target='pendiente']")
        button_cancelados = fox_driver.find_element(By.CSS_SELECTOR, "button[data-target='cancelado']")
        
        data_de_todos = get_data_from_current_table(table)
        
        button_pagados.click()
        data_de_pagados = get_data_from_current_table(table)
        
        button_cancelados.click()
        data_de_cancelados = get_data_from_current_table(table)
        
        button_pendientes.click()
        data_de_pendientes = get_data_from_current_table(table)
        
        print("\nData de todos: \n")
        display_table_data(data_de_todos)
        store_data_in_csv_file(data_de_todos, "data_todos.csv")
        
        print("\nData de pagados: \n")
        display_table_data(data_de_pagados)
        store_data_in_csv_file(data_de_pagados, "data_pagados.csv")
        
        print("\nData de cancelados: \n")
        display_table_data(data_de_cancelados)
        store_data_in_csv_file(data_de_cancelados, "data_cancelados.csv")
        
        print("\nData de pendientes: \n")
        display_table_data(data_de_pendientes)
        store_data_in_csv_file(data_de_pendientes, "data_pendientes.csv")
    
    except Exception as e:
        raise e
    
    finally:
        sleep(3)
        fox_driver.close()

def get_data_from_current_table(table):
    """Get all data related to a type of information."""
    
    # Define data rows with headers
    data_rows = [
        [
            "Selected",
            "Favourite",
            "Type",
            "Title",
            "Subtitle",
            "Color",
            "Date"
        ]
    ]
    
    # Get table rows whose style is not display none
    row_elements = table.find_elements(By.CSS_SELECTOR, "tr:not([style*='display: none'])")
    
    # Loop through each row element
    for row_element in row_elements:
        
        # Make an array to represent data of this row
        row_data = []
        
        # If the row has the class selected, then selected is true, otherwise it is false
        is_selected = True if row_element.get_attribute("class") == "selected" else False
        row_data.append(str(is_selected))
        
        # Grab the a link that has the star class
        star_a = row_element.find_element(By.CSS_SELECTOR, "a.star")
        
        # If star is clicked, then favourite is true, otherwise it is false
        is_favourite = True if "star-checked" in star_a.get_attribute("class") else False
        row_data.append(str(is_favourite))
        
        # Get the type of data from this row
        data_type = row_element.get_attribute("data-status")
        row_data.append(data_type)
        
        # Get the title from this row
        title = row_element.find_element(By.TAG_NAME, "h4").text
        row_data.append(title.split("\n")[0])
        
        # Get the subtitle from this row
        subtitle = row_element.find_element(By.CSS_SELECTOR, "p.summary").text
        row_data.append(subtitle)
        
        # Get the color from this row
        color = row_element.find_element(By.CSS_SELECTOR, "span.pull-right").text[1:-1]
        row_data.append(color)
        
        # Get the date from this row
        date = row_element.find_element(By.CSS_SELECTOR, "span.media-meta.pull-right").text
        row_data.append(date)
        
        # Append this row of data to the rows of data
        data_rows.append(row_data)
        
    return data_rows

def check_row_boxes(table, *row_indexes):
    """Check checkboxes of requested rows of data"""
    
    row_elements = table.find_elements(By.CSS_SELECTOR, "tr:not([style*='display: none'])")
    useful_row_elements = [row_elements[row_index] for row_index in row_indexes]
    
    for useful_row_element in useful_row_elements:
        
        # Get the checkbox for each useful row
        checkbox_input = useful_row_element.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
        
        # Grab the ID of this input element
        checkbox_id = checkbox_input.get_attribute("id")
        
        # Get the label of this input element and click it
        checkbox_label = useful_row_element.find_element(By.CSS_SELECTOR, f"label[for='{checkbox_id}']")
        
        checkbox_label.click()

def click_favourite_link(table, *row_indexes):
    """Toggle between favourite and not favourite of certain row indexes."""
    
    row_elements = table.find_elements(By.CSS_SELECTOR, "tr:not([style*='display: none'])")
    useful_row_elements = [row_elements[row_index] for row_index in row_indexes]
    
    for useful_row_element in useful_row_elements:
        
        # Get the favourite link for each useful row
        favourite_link = useful_row_element.find_element(By.CSS_SELECTOR, "a.star")
        
        # Click the link
        favourite_link.click()

def display_table_data(table_data):
    """Display table data to STDOUT."""
    
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