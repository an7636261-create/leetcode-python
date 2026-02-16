#The problem uses Two Pointer Algorithm
def moveZeroes(nums):
    slow=0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[slow], nums[i] = nums[i], nums[slow] #swapping
            slow+=1

#example
nums=[0,1,0,3,12]
result=moveZeroes(nums)
print("Result:",result)