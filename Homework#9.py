
import string

my_data=[input("Enter a string: ")]
max_lenght=140

for my_string in my_data:
    my_string = my_string.title().replace(" ", "")
    for symbol in string.punctuation:
        my_string = my_string.replace(symbol, "")

    my_string = "#" + my_string

    if len(my_string) > max_lenght:
        print(f"{my_string} is longer than {max_lenght} symbols. It will be shortened.")
        my_string = my_string[:max_lenght]
    print(my_string)