class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        result = []

        def dfs(row,col,visited,prev):
            if row < 0 or row >= rows or col < 0 or col >= cols or (row,col) in visited or heights[row][col] < prev:
                return
            
            visited.add((row,col))
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])


        for c in range(cols):
            dfs(0, c, pac, heights[0][c])  # 1st row is all pacific ocean
            dfs(rows - 1, c, atl, heights[rows - 1][c]) # last row is all atlantic ocean

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0]) # 1st column is all pacific ocean
            dfs(r, cols - 1, atl, heights[r][cols - 1]) # last column is all atlantic ocean

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    result.append([r, c])
        return result