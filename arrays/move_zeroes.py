def moveZeroes(nums):
    slow=0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[slow], nums[i] = nums[i], nums[slow]
            slow+=1

nums=[0,1,0,3,12]
moveZeroes(nums)
print("Result:",nums)