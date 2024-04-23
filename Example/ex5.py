#write a python program to find the sum of all number in list
def find_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers_list = [1, 2, 3, 4, 5]

result_sum = find_sum(numbers_list)
print("Sum of the numbers in the list:", result_sum)