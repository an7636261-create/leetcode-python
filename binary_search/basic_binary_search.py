def binarySearch(nums,target):
    left = 0
    right = len(nums) -1

    while left <= right :
        mid = (left + right) // 2   #here mid is (0+5)//2 -> nums[2] = 3

        if nums[mid] == target:     # 3 == 9 -> False
            return  mid
        if nums[mid] < target:      # 3 < 9 -> True
            left = mid + 1          #left =  left = 2+1 = 3 (search continues)
        else:
            right = mid - 1       
    return -1

#example
nums =[-1,0,3,5,9,12]
target = 9
result = binarySearch(nums,target)
print(result)
