def decimal_to_binary(decimal_num):
    if decimal_num < 0:
        return "Input must be a non-negative integer."
    elif decimal_num == 0:
        return "Binary: 0b0"
    else:
        binary_result = ""
        original_num = decimal_num

        while decimal_num > 0:
            remainder = decimal_num % 2
            binary_result = str(remainder) + binary_result
            decimal_num //= 2

        return f"The binary representation of {original_num} is: 0b{binary_result}"

user_input = int(input("Enter a non-negative integer: "))
binary_representation = decimal_to_binary(user_input)
print(binary_representation)
