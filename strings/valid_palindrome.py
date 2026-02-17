def is_palindrome(s):
    left,right=0,len(s)-1

    while left<right: #keep checking the characters untill the two pointers meet
        while left<right and not s[left].isalnum(): #isalnum() - remove alphanumeric characters
            left+=1
        while left<right and not s[right].isalnum():
            right-=1
        
        if s[left].lower() != s[right].lower():
            return False

        left+=1
        right-=1
    return True

s="A man, a plan, a canal: Panama" #amanaplanacanalpanama
print("Result:",is_palindrome(s))