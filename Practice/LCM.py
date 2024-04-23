import math

def find_lcm(x, y):
    # Calculate the GCD using math.gcd
    gcd = math.gcd(x, y)
    
    # Calculate the LCM using the formula: LCM = (x * y) / GCD
    lcm = (x * y) // gcd
    
    return lcm

# Example usage:
num1 = 12
num2 = 18

result = find_lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {result}")
