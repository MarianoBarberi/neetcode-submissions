class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0]) - 1
        correct_matrix = -1

        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                correct_matrix = i
        
        if correct_matrix == -1:
            return False

        while l <= r:
            m = l + ((r - l) // 2)

            if matrix[correct_matrix][m] < target:
                l = m + 1
            elif matrix[correct_matrix][m] > target:
                r = m - 1
            else:
                return True
        return False