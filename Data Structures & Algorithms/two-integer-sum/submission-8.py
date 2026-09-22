class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} #key = n value = index
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff],i]
            hashMap[n] = i
        
        