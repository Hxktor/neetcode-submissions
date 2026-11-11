class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Top and bottom row
        top, bottom = 0, len(matrix) - 1

        # Binary search to find the correct row
        while top <= bottom:
            row = (top + bottom) // 2

            if target > matrix[row][-1]:
                top = row + 1

            elif target < matrix[row][0]:
                bottom = row - 1

            else:
                break

        # No valid row was found
        if top > bottom:
            return False

        # Binary search inside the selected row
        left, right = 0, len(matrix[row]) - 1

        while left <= right:
            mid = (left + right) // 2

            if target > matrix[row][mid]:
                left = mid + 1

            elif target < matrix[row][mid]:
                right = mid - 1

            else:
                return True

        return False
