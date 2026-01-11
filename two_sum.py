def twoSum(self,nums,target):
    seen={}

    for i,num in enumerate(nums):
        need = target - num
        if need in seen:
            return[seen[num],i]
            seen[num]=i