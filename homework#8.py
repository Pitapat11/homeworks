nums= [1,3,4]
even_nums=0

if not nums:
    print(0)
else:
    for i in range(0, len(nums), 2):
        even_nums+=nums[i]*nums[-1]
        # print(nums[i], end=' ')
    print("Result:",even_nums)