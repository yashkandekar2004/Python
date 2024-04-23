def octal_to_hexadecimal(octal_num):
   
    decimal_num = int(str(octal_num), 8)

    hexadecimal_result = hex(decimal_num)

    return f"The hexadecimal representation of {octal_num} is: {hexadecimal_result}"

 
octal_number = "74"  
hexadecimal_representation = octal_to_hexadecimal(octal_number)
print(hexadecimal_representation)
