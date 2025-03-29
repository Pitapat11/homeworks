def common_elements():
    multiplies_3 = {x for x in range(100) if x % 3 == 0}
    multiplies_5 = {x for x in range(100) if x % 5 == 0}

    return multiplies_3 & multiplies_5
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print(common_elements())