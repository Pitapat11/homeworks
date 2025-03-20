while True:

    first_digit = int(input("enter the first digit: "))
    second_digit = int(input("enter the second digit: "))
    operation = input("select operation (+, -, /, *): ")

    match (operation, second_digit):
       case ("+",_):
           print("Result:", first_digit + second_digit)
       case ("-",_):
           print("Result:", first_digit - second_digit)
       case ("*",_):
           print("Result:", first_digit * second_digit)
       case ("/", 0):
           print("Error: Division by zero")
       case ("/",_):
           print("Result:", first_digit / second_digit)
       case _:
           print("Invalid operation")

    continue_choice = input("Do you want to continue? (yes/no): ")
    if continue_choice != 'yes':
        print("Goodbye!")
        break