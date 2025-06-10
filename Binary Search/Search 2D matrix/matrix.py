class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search column,
        # binary search rows

        rows,cols = len(matrix) - 1, len(matrix[0]) - 1
        l1, r1 = 0,rows
        l2, r2 = 0,cols

        while l1 <= r1:
            mid = l1 + ((r1 - l1) // 2)

            if matrix[mid][0] > target:
                r1 = mid - 1
            elif matrix[mid][0] < target:
                l1 = mid + 1
            else:
                return True

        # Check if we have a valid row
        if r1 < 0:
            return False

        while l2 <= r2:
            mid = l2 + ((r2 - l2) // 2)

            if matrix[r1][mid] > target:
                r2 = mid - 1
            elif matrix[r1][mid] < target:
                l2 = mid + 1
            else:
                return True

        return False