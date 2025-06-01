class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];
        if (nums.length == 2) return Math.max(nums[0], nums[1]);
        if (nums.length == 3) return Math.max(nums[0], Math.max(nums[1], nums[2]));

        int[] first = Arrays.copyOfRange(nums, 0, nums.length - 1);
        int[] last = Arrays.copyOfRange(nums, 1, nums.length);

        return Math.max(helper(first), helper(last));
    }

        private int helper(int[] arr){
            int n = arr.length;
            if (n == 1){
                return arr[0];
            } else if (n == 2){
                return Math.max(arr[0],arr[1]);
            }

            int [] dp = new int[n];
            dp[0] = arr[0];
            dp[1] = Math.max(arr[0],arr[1]);

            for (int i = 2; i < n; i++ ){
                dp[i] = Math.max(dp[i-2] + arr[i],dp[i-1]);
            }
            return dp[n - 1];
        }
    }
