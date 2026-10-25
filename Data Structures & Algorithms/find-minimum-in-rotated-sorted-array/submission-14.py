class Solution:
    def findMin(self, nums: List[int]) -> int:
        #binary search
        l, r  = 0, len(nums) - 1
        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]
        