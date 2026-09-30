class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l,r = 0, len(numbers)-1

        while l<r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l+=1
            else:
                return [numbers[l],numbers[r]]
        return [-1,-1]
        