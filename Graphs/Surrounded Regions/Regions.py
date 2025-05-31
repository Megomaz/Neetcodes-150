class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(row,col):
            if (row < 0 or row >= rows) or (col < 0 or col >= cols) or board[row][col] != "O":
                return

            board[row][col] = "T" #save the square as safe (it wont be transformed)
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and (row in [0,rows-1] or (col in [0,cols-1])): # 2nd condition checks to see if the square is on the border
                    dfs(row,col)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "T":
                    board[row][col] = "O"