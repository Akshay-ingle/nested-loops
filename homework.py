# Program to convert decimal to binary

def decimal_to_binary(decimal_number):
    # Convert decimal to binary using bin() and remove the '0b' prefix
    binary_number = bin(decimal_number).replace("0b", "")
    return binary_number

# Input from the user
decimal_number = int(input("Enter a decimal number: "))

# Convert and display the result
binary_result = decimal_to_binary(decimal_number)
print(f"The binary equivalent of {decimal_number} is {binary_result}")
