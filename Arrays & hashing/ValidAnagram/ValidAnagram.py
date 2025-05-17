class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = {}

        for char in s:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1

        for char in t:
            if char in counter:
                counter[char] -= 1
            else:
                return False
        
        return max(counter.values()) == 0