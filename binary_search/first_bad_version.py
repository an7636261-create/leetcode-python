bad=4

def isBadVersion(version):
    return version >= bad

def firstBadVersion(n):
    left,right = 1,n

    while left < right:
        mid = left + (right - left)//2

        if isBadVersion(mid):
            right = mid       #first bad is at mid or before
        else:
            left = mid + 1   #first bad is after mid

    return left

#example
n=5
result = firstBadVersion(n)
print(result)