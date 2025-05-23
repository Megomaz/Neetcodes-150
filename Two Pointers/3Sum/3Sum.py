class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        nums.sort()
        result = []

        for i in range(size):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = size - 1

            while (l < r):
                if (nums[i] + nums[l] + nums[r] > 0):
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    result.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while (nums[l] == nums[l-1] and l < r):
                        l += 1
                    while (nums[r] == nums[r+1] and r > l):
                        r -= 1
        
        return result