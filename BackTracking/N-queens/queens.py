class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        posDiagonal,negDiagonal = set(),set() # pos = row + col, neg = row - col : pos because as row increases, col decreases; neg because as row increases so does col
        cols = set()
        result = []
        board = [['.'] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                copy = ["".join(row) for row in board] # normal board[:] wont work as we need a joint string 2d list 
                result.append(copy)
                return 

            for col in range(n):
                if (row+col) in posDiagonal or (row-col) in negDiagonal or (col) in cols:
                    continue

                # add the queen to the board
                board[row][col] = 'Q'
                posDiagonal.add(row+col)
                negDiagonal.add(row-col)
                cols.add(col)

                backtrack(row + 1)

                # remove the queen from the board
                board[row][col] = '.'
                posDiagonal.remove(row+col)
                negDiagonal.remove(row-col)
                cols.remove(col)
        backtrack(0)
        return result
            