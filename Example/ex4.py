#write a python program to print the table of the given number using operators
number = int(input("Enter a number: "))

print(f"Multiplication Table for {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")