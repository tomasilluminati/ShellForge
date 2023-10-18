# Import the regular expression module
import re

# Function to check if a string is a valid IP address
def is_ip_address(string):
    # Define a regular expression pattern for matching IP addresses
    ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'

    # Use re.match to check if the string matches the IP pattern
    if re.match(ip_pattern, string):
        return True  # It's a valid IP address
    else:
        return False  # It's not a valid IP address

# Function to test if a given port is within a valid range
def test_port(port):
    try:
        # Attempt to convert the port to an integer
        port = int(port)

        # Check if the port is within the valid range (0-65535)
        if port <= 65535 and port >= 0:
            return True  # It's a valid port
        else:
            return False  # It's not a valid port
    except:
        return False  # An exception occurred, so it's not a valid port

# Function to test if a given number corresponds to a valid language answer
def test_lang_ans(num):
    try:
        # Attempt to convert the number to an integer
        num = int(num)

        # Check if the number is within the valid range (0-64)
        if num <= 64 and num >= 0:  # NOTE: Replace 64 with the actual number of valid shells
            return True  # It's a valid language answer
        else:
            return False  # It's not a valid language answer
    except:
        return False  # An exception occurred, so it's not a valid language answer

# Function to write text to a file with error handling
def write_to_file(text, file_name):
    try:
        # Attempt to open the specified file for writing
        with open(file_name, 'w') as file:
            file.write(text)  # Write the provided text to the file
        print(f'Text has been written to {file_name}')
    except Exception as e:
        print(f'Error writing to the file: {str(e)}')  # Print an error message if writing fails
