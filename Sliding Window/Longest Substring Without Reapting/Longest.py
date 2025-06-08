class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checker = set()
        r = 0
        l = 0
        length = 0

        while (r < len(s)):
            if s[r] in checker:
                length = max(length, len(checker))
                while s[r] in checker:
                    checker.remove(s[l])
                    l += 1
            checker.add(s[r])
            r += 1
        
        return length if len(checker) < length else len(checker)

        