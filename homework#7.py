import random

length = random.randint(3, 10)

random_list = [random.randint(1, 100) for _ in range(length)]
print("Default list:",random_list)

if length >= 3:
    new_list = [random_list[0], random_list[2], random_list[-2]]
    print("New list:", new_list)