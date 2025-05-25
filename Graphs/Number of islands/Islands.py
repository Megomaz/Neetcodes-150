class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0

        def dfs(x,y):
            if  x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid[0]) - 1 or grid[x][y] == "0" or (x,y) in visited:
                return

            visited.add((x,y))         

            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1" and (x,y) not in visited:
                    dfs(x,y)
                    islands += 1

        return islands
            