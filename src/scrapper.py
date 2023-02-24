"""
File to scrap the websites
"""
from typing import Any
from bs4 import BeautifulSoup
import requests
import src.util as util

# Load the settings from the util file
settings = util.load_json_configuration()

# To interpret the fields given in settings.json
def interpret_fields(setting_fields:dict[str, str]=settings['fields']):
    """
        This function will interpret the string to give a nested dictionary
        with keys as 'parent tags',
        and values as 'search attributes'
    """
    formatted_fields = {}

    for field_name, coded_string in setting_fields.items():
        # Separate the parent tag and search attributes
        parent_tag, attr_string = coded_string.split('~')

        # Format the attribute string
        key_val_pair = attr_string.split(':')
        # Add this to attributes
        attributes = dict( (key_val_pair,) )

        # Assign the attributes to the parent tag
        formatted_fields[field_name] = (parent_tag, attributes)
    
    return formatted_fields


def scrap_information(url: str) -> dict[str, Any]:

    # Get the fields
    fields = interpret_fields(settings['fields'])

    # Debug about the fetching phase
    print("[DEBUG] fetching item from the website...")

    # Fetch the content of the html page
    html = requests.get(url=url, headers=settings['header'])

    # Create a soup object to find specific elements in
    # the HTML
    soup = BeautifulSoup(html.content, 'html5lib')

    # Fetch the desired information about the product
    product = {}

    for field_name, (parent_tag, attrs) in fields.items():
        product[field_name] = soup.find(parent_tag, attrs=attrs).text.strip()

    # Return the product
    return product


if __name__ == '__main__':
    URL = "https://www.amazon.in/Samsung-Galaxy-Green-256GB-Storage/dp/B0BT9DVZLZ/ref=sr_1_1_sspa?crid=3NYPGWDXJ4EXQ&keywords=s23&qid=1676994848&sprefix=s%2Caps%2C263&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
    product = scrap_information(URL)

    for field, text in product.items():
        print(field.capitalize(), text, sep=':\t')
