import string
import keyword

test_data = ["get!value","some_super_puper_value"]

for variable in test_data:
    if variable:
        if "__" in variable:
            print(f"Error, found double '_' in {variable} variable name")
        elif variable in keyword.kwlist:
            print(f"Error, found {variable} is keyword")
        elif " " in variable or variable[0].isdigit() or not variable.islower():
            print(f"Error, found {variable} in variable name")
        else:
            is_valid = True
            for char in string.punctuation.replace("_", ""):
                if char in variable:
                    print(f"Error, found {char} in {variable} variable name")
                    is_valid = False
                    break

            if is_valid:
                print(f"Keyword {variable} is correct!")
    else:
        print("Incorrect variable length!")