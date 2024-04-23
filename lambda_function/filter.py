my_range = list(range(1, 11))  
even_numbers = list(filter(lambda x: x % 2 == 0, my_range))

odd_numbers = list(filter(lambda x: x % 2 != 0, my_range))

print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
