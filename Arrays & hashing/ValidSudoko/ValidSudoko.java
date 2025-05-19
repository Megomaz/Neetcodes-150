class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, Set<Character>> cols = new HashMap<>();
        Map<Integer, Set<Character>> rows = new HashMap<>();
        Map<Integer, Set<Character>> squares = new HashMap<>();

        for (int i = 0; i < 9; i++){
            for (int j = 0; j < 9; j++){
                if (board[i][j] == '.'){
                    continue;
                }
                char curr = board[i][j];
                int square = (i / 3) * 3 + (j / 3);

                rows.computeIfAbsent(i, x -> new HashSet<>());
                cols.computeIfAbsent(j, x -> new HashSet<>());
                squares.computeIfAbsent(square, x -> new HashSet<>());

                if (rows.get(i).contains(curr) || cols.get(j).contains(curr) || squares.get(square).contains(curr)) {
                    return false;
                }

                rows.get(i).add(curr);
                cols.get(j).add(curr);
                squares.get(square).add(curr);
            }
        }
        return true;
    }
}
