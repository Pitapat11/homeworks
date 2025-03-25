
import string

STRING_LETTER = string.ascii_letters
SEP= "-"

user_text = input("enter a string like in format 'a-c':  ")

if len(user_text) == 3:
    first_letter = user_text[0]
    sep=user_text[1]
    second_letter = user_text[2]

    if first_letter.isalpha() and sep == SEP and second_letter.isalpha():
        start_index=STRING_LETTER.index(first_letter)
        end_index=STRING_LETTER.index(second_letter)+1
        result = STRING_LETTER[start_index:end_index]
        print(result)