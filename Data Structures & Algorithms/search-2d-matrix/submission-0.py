class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        row = -1

        # Step 1: Find the row that could contain target
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][-1]:
                row = i
                break

        # Target doesn't fall within any row
        if row == -1:
            return False

        # Step 2: Binary search the selected row
        l = 0
        r = len(matrix[row]) - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[row][mid] == target:
                return True

            elif matrix[row][mid] < target:
                l = mid + 1

            else:
                r = mid - 1

        return False


        

        