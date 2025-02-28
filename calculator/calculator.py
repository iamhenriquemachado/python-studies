menu_option = int(input("Choose a operation: "))

num1 = int(input("Insert num1: "))
num2 = int(input("Insert num2: "))

def add_numbers(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


if menu_option == 1:
   # Sum
   selected_function = add_numbers
   result = selected_function(num1, num2)
   print("Result: ", result)

elif menu_option == 2:
    # Subtract
   selected_function = subtract
   result = selected_function(num1, num2)
   print("Result: ", result)

elif menu_option == 3:
   selected_function = multiply
   result = selected_function(num1, num2)
   print("Result: ", result)

elif menu_option == 4:
    # Divide 
   selected_function = divide
   result = selected_function(num1, num2)
   print("Result: ", result)

