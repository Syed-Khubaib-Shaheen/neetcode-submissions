
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid_row = (top + bottom) // 2

            if target < matrix[mid_row][0]:
                bottom = mid_row - 1

            elif target > matrix[mid_row][-1]:
                top = mid_row + 1

            else:
                left = 0
                right = len(matrix[mid_row]) - 1

                while left <= right:
                    mid_col = (left + right) // 2

                    if matrix[mid_row][mid_col] == target:
                        return True

                    elif matrix[mid_row][mid_col] > target:
                        right = mid_col - 1

                    else:
                        left = mid_col + 1

                return False

        return False
