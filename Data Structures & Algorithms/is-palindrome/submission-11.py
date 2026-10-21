class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = s.lower()
        final_s=""
        for c in new_s:
            if c.isalnum():
                final_s += c
        

        l,r = 0, len(final_s) - 1
        while l<=r:
            if final_s[l] != final_s[r]:
                return False
            l+=1
            r-=1
        return True
