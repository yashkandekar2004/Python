def convert_result(data_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                converted_result = data_type(result)
                return converted_result
            except ValueError:
                print(f"Error converting result to {data_type}")
                return None

        return wrapper

    return decorator

@convert_result_to(int)
def multiply(a, b):
    return a * b

@convert_result_to(float)
def divide(a, b):
    return a / b

# Test the decorated functions

result_int = multiply(5, 3)  # Should return 15 as an integer
print(f"Result (int): {result_int}")

result_float = divide(10, 2)  # Should return 5.0 as a float
print(f"Result (float): {result_float}")
