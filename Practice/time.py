import time

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.4f} seconds")
        return result

    return wrapper

# Example usage:

@measure_execution_time
def example_function():
    # Simulate some time-consuming task
    time.sleep(2)
    print("Function executed!")

# Test the decorated function
example_function()
