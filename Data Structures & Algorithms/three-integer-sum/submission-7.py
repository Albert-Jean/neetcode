class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        # fix value        
        n = len(nums)
        for i in range(n):
            #two pointer on the two remaining 
            target = - nums[i]
            twoPointer = self.twoPointer(nums,i+1,n-1,target)
            if i==0 and twoPointer != []:
                res.append(twoPointer)
            elif i>0 and twoPointer != [] and res[i-1]!=twoPointer:                                
                res.append(twoPointer)
            else:
                continue
        return res
    
    def twoPointer(self, nums: List[int], left : int, right: int, target: int) -> List[int]:
        while (left < right):            
            res = nums[left] + nums[right]
            if res == target:
                return [-target,nums[left],nums[right]]
            if res > target:
                right -= 1
            else:
                left += 1 
        return []
            



        