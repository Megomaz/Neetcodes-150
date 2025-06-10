class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hashmap = defaultdict(int)
        max_count = 0
        

        for r in range(len(s)):
            hashmap[s[r]] += 1

            while hashmap[s[r]] >= 2:
                hashmap[s[l]] -= 1
                l += 1

            max_count = max(max_count,r - l + 1)

        return max_count



        