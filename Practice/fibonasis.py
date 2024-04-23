def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please provide a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fibonacci(n - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

sequence_length = 0
fibonacci_sequence = fibonacci(sequence_length)
print(f"The Fibonacci sequence of length {sequence_length} is: {fibonacci_sequence}")
