class Solution:
    def searchMatrix(self, matrix, target):
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            row = matrix[m]
            if row[0] > target:
                r = m - 1
            elif row[-1] < target:
                l = m + 1
            else:
                idx, _, _ = self.binarySearch(row, target)
                if idx != -1:
                    return True
                break  # target was in [row[0], row[-1]] but not found → not in this row, and won't be in any row
        return False


    def binarySearch(self,array: List[int], target: int) -> List[int]:
        l,r = 0, len(array)-1
        while l <= r:
            m = int((l+r)/2)
            if array[m] > target:
                r = m - 1                
            elif array[m] < target:
                l = m + 1
            else:
                return [m,array[0],array[-1]]

        return [-1,array[0],array[-1]]
        