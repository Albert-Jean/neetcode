class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = 1
        res = []
        zeroC = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                prefixProduct *= nums[i]
            else :
                zeroC += 1
        for i in range(n): 
            if zeroC > 1:
                res.append(0)
            elif zeroC == 1:
                res.append(prefixProduct if nums[i] == 0 else 0)
            else:
                res.append(prefixProduct // nums[i])                      
        return res
