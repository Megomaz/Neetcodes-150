class Solution:
    def trap(self, height: List[int]) -> int:
        Max_left = [0] * len(height)
        Max_right = [0] * len(height)
        n = len(height) - 1
        Sum = 0

        for i in range(len(height)):
            Max_left[i] = max(height[i-1],Max_left[i-1]) if i - 1 >= 0 else 0
            Max_right[n - i] = max(height[n - i + 1],Max_right[n - i + 1]) if n - i + 1 < len(height) else 0
        
        for x in range(len(height)):
            Min = min(Max_left[x],Max_right[x])
            Sum += Min - height[x] if Min - height[x] > 0 else 0

        return Sum

# 2 pointer Solution
class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0 ,len(height) - 1
        Sum = 0

        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax,height[l])
                Sum += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(leftMax,height[r])
                Sum += rightMax - height[r]
        return Sum