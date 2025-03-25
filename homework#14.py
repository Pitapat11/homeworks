
user_input=int(input("Enter a number: "))
print(user_input)

while user_input > 9:
    string_number=str(user_input)
    user_input=1
    for char in string_number:
        user_input *= int(char)
        print(char)
    print(user_input)
