def twoSum(nums,target):
    seen={}  #number -> index

    for i,num in enumerate(nums):
        need = target - num
        if need in seen:
            return[seen[num],i]
            seen[num]=i #if the num is not seen ,it stores here as current index
 #example
nums = [2,7,11,15]
target = 9
#9-2 = 7 -> not seen
#9-7 = 2 -> seen, so seen[2],i this returns [0,1]

#Here key idea is "Before starting a number,check if it's parter already exists"