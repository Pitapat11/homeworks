
num=int(input('enter 4 digits : '))

thousands = num // 1000
hundreds = num %1000 // 100
tens = num % 100 // 10
ones = num % 10

print(thousands)
print(hundreds)
print(tens)
print(ones)