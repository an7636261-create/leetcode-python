def minEatingSpeed(piles,h):
    left = 1
    right = max(piles)

    while left < right :
        mid = (left + right) // 2
        
        hours = 0
        for p in piles:
            hours += (p + mid - 1) // mid  #ceil=(p/mid)
        if hours <= h:
            right = mid   #try slower speed
        else:
            left = mid +1  #try faster speed
    return left

#example
piles = [3,6,7,11]
h = 8
print(minEatingSpeed(piles,h))