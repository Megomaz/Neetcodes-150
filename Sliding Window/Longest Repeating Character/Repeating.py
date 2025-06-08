class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_freq = 0
        count = 0
        hashmap = defaultdict(int)

        for r in range(len(s)):
            hashmap[s[r]] += 1
            max_freq = max(max_freq, hashmap[s[r]])

            # If window size - max char count > k, shrink window
            while (r - l + 1) - max_freq > k:
                hashmap[s[l]] -= 1
                l += 1

            count = max(count, r - l + 1)

        return count