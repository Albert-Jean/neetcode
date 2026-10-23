class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = nums1 + nums2
        nums1.sort()
        i = int(len(nums1)/2)
        if len(nums1) % 2 == 0:
            res = float((nums1[i-1]+nums1[i])/2)
        else:
            res = float(nums1[int(len(nums1)/2)])
        return res
        
        