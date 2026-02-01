def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left]) #remove left duplicate char
            left+=1 #and move forward
        char_set.add(s[right]) #now add right char(unique)
        max_len=max(max_len,right-left+1) #(right-left+1)is the current max length

    return max_len

#example
s="abcabcbb"
print("Result",lengthOfLongestSubstring(s))