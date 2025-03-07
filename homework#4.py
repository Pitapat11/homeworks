nums = [1,2,3,4,5,6]
middle_indexlist = len(nums) // 2

if len(nums) % 2 != 0:
    middle_indexlist += 1

half1 = nums[:middle_indexlist]
half2 = nums[middle_indexlist:]

result = [half1, half2]
print(result)