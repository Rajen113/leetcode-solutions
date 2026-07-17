class Solution(object):
    def isPalindrome(self, s):
        if s == " ":
            return True
        
        temp = "".join(ch.lower() for ch in s if ch.isalnum())
        
        left=0
        right=len(temp)-1
        
        while left<right:
            if temp[left] != temp[right]:
                return False
            left+=1
            right-=1
        return True