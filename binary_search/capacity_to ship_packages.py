def shipWithinDays(weights,days):
    def canShip(capacity):
        current = 0
        needed_days = 1 

        for w in weights:
            if current + w > capacity:
                needed_days += 1
                current = w
            else:
                current += w
        return needed_days <= days
    
    left = max(weights)
    right = sum(weights)

    while left <= right:
        mid = (left + right)//2

        if canShip(mid):
            right = mid - 1
        else:
            left = mid+1
    return left

#example
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(shipWithinDays(weights,days))
