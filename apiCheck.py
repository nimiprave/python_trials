import re


def check_api_format(string):
    # Define the regex pattern to match API_SOMENAME
    pattern = r"^API_[A-Za-z_]+$"

    # Use re.search() to check if the pattern exists in the string
    match = re.search(pattern, string)

    # Return True if a match is found, otherwise False
    if match is None:
        raise Exception("API name is not valid")
    return match is not None


if __name__ == "__main__":

    try:
        # Test the function with valid and invalid strings
        print(check_api_format("API_GET_USERS"))  # True
        print(check_api_format("API_jlsfjlsfjds"))  # False
        print(check_api_format("APIGET_USERS_1"))  # False
        print(check_api_format("_APIGET_USERS_1"))  # False

    except Exception as e:
        print(e)
