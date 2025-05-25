class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        rows,cols = len(grid), len(grid[0])
        visited = set()

        def bfs(row,col):
            if row < 0 or row >= rows or col < 0 or col >= cols or (row,col) in visited:
                return

            area = 1

            q = deque()
            visited.add((row,col))
            q.append((row,col))

            while q:
                gr, gc = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + gr, dc + gc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc))      
                        area += 1    
            return area

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row,col) not in visited:
                    area = bfs(row,col)
                    if (area > maxArea):
                        maxArea = area
                        

        return maxArea
