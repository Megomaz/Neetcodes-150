class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        def binarySearch(l,r,arr):

            while l <= r:
                mid = l + ((r - l) // 2)

                if arr[mid] > target:
                    r = mid - 1
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    return mid
            return -1

        res1 = binarySearch(0,l,nums)
        res2 = binarySearch(l,len(nums) - 1,nums)

        return res1 if res1 != -1 else res2