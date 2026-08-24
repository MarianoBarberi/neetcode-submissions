class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i, row in enumerate(matrix):
            if row[-1] > target:
                break
            elif row[-1] == target:
                return True
        
        l = 0
        r = len(matrix[i]) - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[i][mid] < target:
                l = mid + 1
            elif matrix[i][mid] > target:
                r = mid - 1
            else:
                return True
        return False