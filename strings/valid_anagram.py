def isAnagram(s,t):
    return sorted(s) == sorted(t)
        
s="anagram"
t="nagaram"
print("Result:",isAnagram(s,t))

