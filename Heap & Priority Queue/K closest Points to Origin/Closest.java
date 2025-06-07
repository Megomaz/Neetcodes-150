class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<double[]> minHeap = new PriorityQueue<>(
    (a, b) -> Double.compare(a[1], b[1])
        );

        int index = 0;
        int[][] result = new int[k][2];  // you want k points, not length of all points

        for (int[] point : points) {
            double res = Math.sqrt(Math.pow(point[0], 2) + Math.pow(point[1], 2));
            minHeap.add(new double[] {index, res});
            index++;
        }

        for (int i = 0; i < k; i++) {
            double[] top = minHeap.poll();
            int idx = (int) top[0];
            result[i][0] = points[idx][0];
            result[i][1] = points[idx][1];
        }

        return result;
                
    }
}
