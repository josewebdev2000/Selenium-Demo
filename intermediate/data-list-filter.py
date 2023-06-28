# Solution for Data List Filter Intermediate Exercise
from selenium.webdriver.common.by import By

from utils import helpers, constants

from time import sleep

def main():
    
    fox_driver = helpers.get_firefox_driver("-headless")
    
    fox_driver.get(constants.DATA_LIST_FILTER_DEMO)
    
    try:
        # Grab common DOM elements to use throughout the script
        input_search_box = fox_driver.find_element(By.ID, "input-search")
        info_container = fox_driver.find_element(By.CLASS_NAME, "searchable-container")
        
        # Search for information in the filtered box
        
        # First packets of information for "Br" as keyword
        packets = get_filtered_information(input_search_box, info_container, "Br")
        display_analyzed_data(packets)
        
        # Second packet of information for "Arman" as keyword
        packets = get_filtered_information(input_search_box, info_container, "Arman")
        display_analyzed_data(packets)
    
    except Exception as e:
        pass
    
    finally:
        sleep(3)
        fox_driver.close()


def get_filtered_information(input_search, container, keyword):
    """Enter a keyword to an input search component 
    and then display the information found in the container."""
    
    # Store the found info in packets (dictionaries)
    info_packets = []
    
    # Send the keyword to the input search
    input_search.send_keys(keyword)
    
    # Grab the children of the container whose style selector is [style='display: block;']
    filtered_boxes = container.find_elements(By.CSS_SELECTOR, "div[style='display: block;']")
    
    # If there is no information found, return an empty list
    if len(filtered_boxes) < 1:
        return info_packets
    
    # Loop through the list of filtered boxes
    for box in filtered_boxes:
        
        # Get div that contains the info we look for
        info_box = box.find_element(By.CLASS_NAME, "info-block")
        
        # Get the info from that div
        info_packet = get_info_packet_from_div(info_box)
        
        # Append info packet to list of info packets
        info_packets.append(info_packet)
        
    # Clean out the input after the search
    input_search.clear()
    
    # return the info packets
    return info_packets


def get_info_packet_from_div(info_div):
    """Return a Dictionary that stores information found in a particular info div."""
    
    # Final dict to return
    info_dict = {}
    
    info_dict["company_name"] = get_str_after_semicolon(info_div.find_element(By.TAG_NAME, "h5").text)
    info_dict["person_name"] = get_str_after_semicolon(info_div.find_element(By.TAG_NAME, "h4").text)
    info_dict["job_title"] = get_str_after_semicolon(info_div.find_element(By.TAG_NAME, "p").text)
    info_dict["phone_number"] = get_str_after_semicolon(info_div.find_element(By.CSS_SELECTOR, "div > span:nth-child(5)").text)
    info_dict["email"] = get_str_after_semicolon(info_div.find_element(By.CSS_SELECTOR, "div > span:nth-child(6)").text)
    
    return info_dict

def get_str_after_semicolon(str_with_semicolon):
    """Return the part of the string that comes after the semi colon."""
    
    if ":" in str_with_semicolon:
        return str_with_semicolon.split(":")[1]
    
    else:
        return str_with_semicolon

def display_analyzed_data(info_packets):
    """Received info packets and show them to the console."""
    
    counter = 0
    
    print("\nInformation Filtered: \n")
        
    # Print each box 
    for packet in info_packets:
        counter += 1
        print(f"Person No: {counter} \n")
        print(f"Name: {packet['person_name']}")
        print(f"Company Name: {packet['company_name']}")
        print(f"Job Title: {packet['job_title']}")
        print(f"Phone Number: {packet['phone_number']}")
        print(f"Email Address: {packet['email']}")
        print("\n")

if __name__ == "__main__":
    main()