def find_hcf(x, y):
    # Ensure x is greater than y
    if x < y:
        x, y = y, x

    while y:
        x, y = y, x % y

    return x

# Example usage:
num1 = 12
num2 = 18

result = find_hcf(num1, num2)
print(f"The HCF of {num1} and {num2} is: {result}")
