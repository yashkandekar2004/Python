# write a python program to get fibaccisies series between number 0 to 75
def generate_fibonacci(limit):
    fibonacci_series = [0, 1]
    while True:
        next_number = fibonacci_series[-1] + fibonacci_series[-2]
        if next_number <= limit:
            fibonacci_series.append(next_number)
        else:
            break
    return fibonacci_series
5
limit = 75

fibonacci_series = generate_fibonacci(limit)
print("Fibonacci series up to", limit, ":", fibonacci_series)