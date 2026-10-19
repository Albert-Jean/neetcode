class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        current_min,current_max =1,1
        for n in nums:
            if n ==0:
                current_min,current_max =1,1
                continue
            temp = current_max*n
            current_max = max(n*current_max,n*current_min,n)
            current_min = min(n*current_min,temp,n)
            res = max(res,current_max,current_min)
        return res

        

        