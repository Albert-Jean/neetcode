class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        s=str(x)

        for i in range(len(s)):
            if s[i] != s[(len(s)-1)-i]:
                return False
        return True
            

        