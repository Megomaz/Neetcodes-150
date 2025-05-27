class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board), len(board[0])
        size = len(word)
        result = False
       
        def dfs(r,c, index ,visited, curr):
            if index == size:
                return True

            if (r >= rows or r < 0) or (c >= cols or c < 0) or (r,c) in visited or index > size - 1:
                return

            if curr == word:
                return True

            if board[r][c] != word[index]:
                return

            curr += board[r][c]
            visited.add((r,c))
        
            print(curr)
            res = (dfs(r+1,c,index+1,visited,curr) or
            dfs(r-1,c,index+1,visited,curr) or
            dfs(r,c+1,index+1,visited,curr) or
            dfs(r,c-1,index+1,visited,curr))

            visited.remove((r,c))
            return res

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0, set(), ""):
                        return True

        return result

        