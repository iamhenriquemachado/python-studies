# 1. Celsius to Farenheit

menu_option = int(input("Choose a convertion - 1 celsius to farenheit or 2 farenheit to celsius \n"))
cont = 'y'

while cont.lower() == 'y':
    if menu_option == 1:
        def celsius_to_farenheit():
            user_input = float(input("Insert the celsius degree: "))
            farenheit_formula = (user_input * (9/5)) + 32
            return print("The weather in farenheit is: ", farenheit_formula)
        selected_function = celsius_to_farenheit


    elif menu_option == 2:
        def farenheit_to_celsius():
            user_input = float(input("Insert the farenheit degree: "))
            celsius_formula = (user_input-32) * (5/9)
            return print("The weather in celsius is: ", celsius_formula)
        selected_function = farenheit_to_celsius

    if selected_function:
        selected_function()
    else:
         print("Invalid input!")
    cont = input("Continue?y/n \n")
    if cont == 'n':
        break

