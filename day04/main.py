import re


def is_valid(password, exact_double=False):
    # Returns (bool) True if password fits criteria
    # Check if it contains a double
    if exact_double:
        search_for = r'(.)\1(?!\1)'
    else:
        search_for = r'(.)\1'
    if not re.match(search_for, password):
        return False

    # Check that it is monotonically increasing
    values = [int(i) for i in str(password)]
    for i in range(len(values) - 1):
        if values[i] > values[i+1]:
            return False

    return True