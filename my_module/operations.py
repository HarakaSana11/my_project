
def do_add(self, s):
    """
    Splits the input string `s` into two components, converts them to integers, and returns their sum.
    
    Args:
        s (str): A string containing two numbers separated by spaces.
        
    Returns:
        int: The sum of the two numbers, or None if there was an error.
    """
    components = s.split()
    if len(components) != 2:
        print("*** Error: Invalid number of arguments. Expected 2 arguments.")
        return None
    try:
        numbers = [int(component) for component in components]
    except ValueError:
        print("*** Error: Arguments should be numbers.")
        return None
    return numbers[0] + numbers[1]
