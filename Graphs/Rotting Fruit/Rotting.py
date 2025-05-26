class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        q = deque()
        rows,cols = len(grid), len(grid[0])
        Fresh = 0
        minutes = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row,col))
                elif grid[row][col] == 1:
                    Fresh += 1
        

        while q and Fresh > 0:
            for i in range(len(q)):  # process one "minute"/ 1 layer of bsf
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        Fresh -= 1
            minutes += 1
        
        if Fresh == 0:
            return minutes
        else:
            return -1
                   
            
            
        