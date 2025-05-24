class Solution {
    public int maxArea(int[] heights) {
        int r = heights.length - 1;
        int l = 0;
        int max = 0;

        while (l < r){
            int mul = Math.min(heights[l],heights[r]) ;
            max = Math.max(max, mul*(r-l));

            if (mul == heights[l]){
                l += 1;
            }else{
                r -= 1;
            }
        }
        return max;
    }
}
