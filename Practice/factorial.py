# using recursion

# def factorial_recursive(n):
 #    if n == 0 or n == 1:
 #        return 1
 #    else:
 #        return n * factorial_recursive(n - 1)

# num = 5
# result_recursive = factorial_recursive(num)
# print(f"The factorial of {num} using recursion is: {result_recursive}")


# Without recursion


def factorial_non_recursive(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = 5
result_non_recursive = factorial_non_recursive(num)
print(f"The factorial of {num} without recursion is: {result_non_recursive}")
