#Basic regex tasks. Write a function that takes in a numeric code of any length.
# The function should check if the code begins with 1, 2, or 3 and return true if so.
# Return false otherwise.

def validate_code(code):
    first_digit = str(code)[0]
    if first_digit == '1':
        return True
    elif first_digit == '2':
        return True
    elif first_digit == '3':
        return True
    else:
        return False