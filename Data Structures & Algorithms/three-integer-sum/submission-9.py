class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        # fix value        
        n = len(nums)
        for i,a in enumerate(nums):
            #two pointer on the two remaining 
            if i > 0 and a == nums[i-1]:
                continue
            target = - nums[i]
            twoPointer = self.twoPointer(nums,i+1,n-1,target)                        
            if twoPointer != []:                                
                res = twoPointer
            else:
                continue
        return res
    
    def twoPointer(self, nums: List[int], left : int, right: int, target: int) -> List[int]:
        resArr = []
        while (left < right):            
            res = nums[left] + nums[right]
            if res == target:
                resArr.append([-target,nums[left],nums[right]])
            if res > target:
                right -= 1
            else:
                left += 1 
        return resArr
            



        