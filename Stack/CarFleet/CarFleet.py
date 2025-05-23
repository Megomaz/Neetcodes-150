class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = list(zip(position,speed))
        zipped.sort(reverse = True, key=lambda x: x[0])
        stack = []

        for i in range(len(zipped)):
            speed = (target - zipped[i][0]) /zipped[i][1]
            if stack and speed <= stack[-1]:
                continue
            else:
                stack.append(speed)

        return len(stack)