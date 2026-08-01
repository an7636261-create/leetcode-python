def defuseBomb(code,k):
    n = len(code)
    ans = []

    for i in range(n):
        total = 0

        if k>0:
            for j in range(1,k+1):
                index = (i+j) % n
                total += code[index]

        elif k>0:
            for j in range(1,abs(k)+1):
                index = (i-j) % n 
                total += code[index]

        else:
            total = 0

        ans.append(total)

    return ans

code = [5,7,1,4]
k = 3 
print(defuseBomb(code,k))