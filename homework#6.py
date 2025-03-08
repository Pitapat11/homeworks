nums= [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
count=nums.count(0)

for _ in range(count):
    nums.remove(0)
    nums.append(0)
print(nums)