import re


def is_valid(password):
    # Returns (bool) True if password fits criteria

    # Check if it contains a double
    if not re.search(r'(.)\1', password):
        return False

    # Check that it is monotonically increasing
    values = [int(i) for i in str(password)]
    for i in range(len(values) - 1):
        if values[i] > values[i+1]:
            return False

    return True