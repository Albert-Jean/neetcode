class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l,r = 0 , n-1
        while(l < r):
            twosum = numbers[l] + numbers[r]
            if twosum == target:
                return [numbers[l],numbers[r]]
            if twosum > target:
                r -= 1
            else:
                l += 1
        return [-1,-1]
