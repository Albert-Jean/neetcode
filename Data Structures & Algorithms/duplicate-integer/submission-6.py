class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap:
                return True
            hashMap[nums[i]] = i
        return False
            
        