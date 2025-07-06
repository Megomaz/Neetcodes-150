#Leetcode hard backtrack
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3) * 3 + (c // 3)].add(val)

        def backtrack(row,col):
            if col == 9:
                return backtrack(row+1,0)
                 
            if row == 9:
                return True

            if board[row][col] != '.':
                return backtrack(row, col + 1)

            for num in map(str, range(1, 10)):
                if num in rows[row] or num in cols[col] or num in boxes[(row // 3) * 3 + (col // 3)]:
                    continue

                #add to board
                board[row][col] = num
                rows[row].add(num)
                cols[col].add(num)
                boxes[(row // 3) * 3 + (col // 3)].add(num)

                if backtrack(row, col + 1):
                    return True

                #remove from board
                board[row][col] = '.'
                rows[row].remove(num)
                cols[col].remove(num)
                boxes[(row // 3) * 3 + (col // 3)].remove(num)
            return False

        backtrack(0,0)


        