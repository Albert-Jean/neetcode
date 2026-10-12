class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixSum = 1
        zeroC = 0
        for num in nums:
            if num != 0:
                prefixSum *= num
            else:
                zeroC += 1
        res=[]
        for i in range(len(nums)):
            if zeroC > 1:
                res.append(0)
            elif zeroC == 1:
                res.append(prefixSum if nums[i] == 0 else 0)
            else:
                res.append(prefixSum // nums[i])
        return res
        