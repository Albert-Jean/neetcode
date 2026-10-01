class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        #Merge two arrays + sort
        # if m+n % 2 == 0 -> pair med = (m+l/2) / 2
        #else med = middle of array
        for num in nums2:
            nums1.append(num)
        nums1.sort()
        i = int(len(nums1)/2)
        if len(nums1) % 2 == 0:
            res = float((nums1[i-1]+nums1[i])/2)
        else:
            res = float(nums1[int(len(nums1)/2)])
        return res
        
        