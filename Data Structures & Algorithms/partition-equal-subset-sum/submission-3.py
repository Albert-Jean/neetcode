class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #compute total sum
        totalSum = sum(nums)
        #find subset with sum == totalSum / 2 -> obv if totalSum%2 != 0 return False
        if totalSum % 2 != 0:
            return False   

        target = totalSum // 2
        dp = {0}
        for n in nums:
            next_dp = set(dp)
            for s in dp:
                if s + n == target:
                    return True
                if s + n < target:
                    next_dp.add(s + n)
            dp = next_dp
            
        return target in dp
        