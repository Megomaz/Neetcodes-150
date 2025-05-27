class Solution {
    public int findMin(int[] nums) {
        int l = 0;
        int r = nums.length - 1;
        int result = nums[0];

        while (l <= r){
            if (nums[l] < nums[r]){
                result = Math.min(result,nums[l]);
                break; 
            }
            
            int mid = (r + l) /2;
            result = Math.min(result, nums[mid]);

            if (nums[mid] >= nums[l]){
                l = mid + 1;
            }else{
                r = mid - 1;
            }

        }
        return result;
    }
}
