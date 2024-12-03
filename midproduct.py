def product_of_middle_digits(number):
    # Convert the number to a string to easily access its digits
    num_str = str(number)
    length = len(num_str)

    # If the number has less than 2 digits, there are no "middle digits"
    if length < 2:
        print("The number does not have enough digits for middle calculation.")
        return None

    # Determine if the number has an even or odd number of digits
    if length % 2 == 0:
        # Even number of digits, get the two middle digits
        middle1 = int(num_str[length // 2 - 1])
        middle2 = int(num_str[length // 2])
        product = middle1 * middle2
    else:
        # Odd number of digits, take the single middle digit
        middle = int(num_str[length // 2])
        product = middle

    return product


# Input from the user
try:
    number = int(input("Enter a number: "))
    if number < 0:
        print("Please enter a non-negative number.")
    else:
        result = product_of_middle_digits(number)
        if result is not None:
            print(f"The product of the middle digits is: {result}")
except ValueError:
    print("Invalid input. Please enter an integer.")
