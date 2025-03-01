num = int(input("enter 5 digit number: "))

ten_ths = num // 10000
thous = (num % 10000) // 1000
hunds = (num % 1000) // 100
tens = (num % 100) // 10
ones = num % 10

result = ones * 10000 + tens * 1000 + hunds * 100 + thous * 10 + ten_ths

print(result)
