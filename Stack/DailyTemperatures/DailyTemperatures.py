class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i,temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                result[stack[-1][0]] = i - stack[-1][0] 
                stack.pop()
            else:
                stack.append((i,temp))

        return result