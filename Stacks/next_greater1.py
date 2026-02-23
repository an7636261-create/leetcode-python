def nextgreater(nums1,nums2):
    stack = []
    next_greater = {} #dictionary (hash map)
    
    #process nums2
    for num in nums2:
        while stack and num > stack[-1]:
            prev = stack.pop()
            next_greater[prev] = num

        #we may find a grater element later,we don't know yet
        stack.append(num)
        
    #elements left in stack have no next greater so return -1
    for num in stack:
        next_greater[num] = -1

    #build result for nums1 
    return[next_greater[num] for num in nums1]

#example
nums1 = [4,1,2] 
nums2 = [1,3,4,2]
result = nextgreater(nums1, nums2)
print(result)