def check_even_odd(number):
    """
    Checks if a number is even or odd.
    
    Parameters:
    number (int): The number to check.
    
    Returns:
    str: "Even" if the number is even, "Odd" if odd.
    """
    if number % 2 == 0:  # If the remainder of division by 2 is 0, it's even
        return "Even"
    else:
        return "Odd"

def convert_temperature(celsius):
    """
    Converts temperature from Celsius to Fahrenheit, with validation for values below zero.
    
    Parameters:
    celsius (float): Temperature in degrees Celsius.
    
    Returns:
    str: Error message if below zero, or the conversion to Fahrenheit.
    """
    if celsius < 0:
        return "Temperature below zero"
    else:
        fahrenheit = (celsius * 9/5) + 32  # Standard conversion formula
        return f"{celsius}°C is equal to {fahrenheit}°F"

def add(a, b):
    """
    Adds two numbers.
    
    Parameters:
    a (float): First number.
    b (float): Second number.
    
    Returns:
    float: The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Subtracts the second number from the first.
    
    Parameters:
    a (float): The number to subtract from.
    b (float): The number to subtract.
    
    Returns:
    float: The difference a - b.
    """
    return a - b

def multiply(a, b):
    """
    Multiplies two numbers.
    
    Parameters:
    a (float): First number.
    b (float): Second number.
    
    Returns:
    float: The product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Divides the first number by the second, with division by zero check.
    
    Parameters:
    a (float): Dividend.
    b (float): Divisor.
    
    Returns:
    float or str: The quotient if b != 0, or an error message.
    """
    if b == 0:
        return "Error: division by zero."
    return a / b