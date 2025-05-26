class Solution {
    public void islandsAndTreasure(int[][] grid) {
        int[][] directions = {{0,1},{0,-1},{1,0},{-1,0}};
        Deque<int[]> q = new ArrayDeque<>();
        int rows = grid.length;
        int cols = grid[0].length;


        for (int row = 0; row < rows; row++){
            for (int col = 0; col < cols; col++){
                if (grid[row][col] == 0){
                    q.add(new int[]{row, col});
                }
            }
        }

        while (!q.isEmpty()){
            int[] coords = q.poll();  

            for (int[] dir : directions) {
                int dr = dir[0];
                int dc = dir[1];
                
                int nr = dr + coords[0];
                int nc = dc + coords[1];

                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 2147483647){
                    grid[nr][nc] = 1 + grid[coords[0]][coords[1]];
                    q.add(new int[] {nr,nc});
                }
            }
        }
    }
}
