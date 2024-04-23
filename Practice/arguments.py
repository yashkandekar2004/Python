def log_arguments_and_return(func):
    def wrapper(*args, **kwargs):
        # Log the arguments
        print(f"Arguments: {args}, {kwargs}")

        # Call the original function
        result = func(*args, **kwargs)

        # Log the return value
        print(f"Return value: {result}")

        return result

    return wrapper

# Example usage:

@log_arguments_and_return
def add_numbers(a, b):
    return a + b

@log_arguments_and_return
def multiply_numbers(x, y):
    return x * y

# Test the decorated functions

add_result = add_numbers(3, 5)
multiply_result = multiply_numbers(4, 6)
