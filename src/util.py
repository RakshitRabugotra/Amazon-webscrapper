"""
The utilities file for the project
"""
import json

def load_json_configuration(json_file_pointer="./settings.json"):
    """
        This function will read the essential details provided
        in the JSON file and load them into a dictionary
    """
    json_object = {}
    try:
        with open(json_file_pointer, 'r') as json_file:
            # Read from the file
            json_object = json.load(json_file)
    except FileNotFoundError as ff_error:
        print("[ERROR]:", ff_error, "\nLoading from failsafe...")
        # Load configuration from the failsafe file
        load_json_configuration("./failsafe/failsafe_constants.json")
    except Exception as e:
        print("[ERROR]:", e)
    
    return json_object

def write_json_configuration(dict_object, json_file_pointer) -> int:
    """
        Write the data of dictionary to a json file
    """
    try:
        # Writing in Serialized way
        json_object = json.dumps(dict_object, indent=4)

        with open(json_file_pointer, mode='w') as output_json:
            output_json.write(json_object)
        
        # Successful execution
        return 0
    except Exception as e:
        print("[ERROR]:", e)
    
    # Unsuccessful execution
    return -1

"""
Load configuration form the settings
"""
settings = load_json_configuration("./settings.json")
