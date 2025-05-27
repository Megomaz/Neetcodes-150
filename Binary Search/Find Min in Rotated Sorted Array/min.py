class Solution:
    def findMin(self, nums: List[int]) -> int:
        size = len(nums) - 1
        l,r = 0, len(nums) - 1
        low = nums[0]

        while (l <= r):
            mid = (l + r) // 2
            if mid+1 < size and nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            elif mid-1 >= 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif nums[mid] >= low:
                l = mid + 1
            else:
                r = mid - 1
        return low
