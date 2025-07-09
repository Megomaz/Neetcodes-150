class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        seen = set()

        hashmap = defaultdict(int)
        for index,char in enumerate(s):
            if char not in seen:
                hashmap[char] = [index,index]
                seen.add(char)
            else:
                hashmap[char][1] = index

        arr = []

        for interval in hashmap.values():
            if arr and arr[-1][1] > interval[0]:
                arr[-1][0], arr[-1][1] = min(arr[-1][0],interval[0]), max(arr[-1][1],interval[1])
                continue
            arr.append(interval)

        for i in range(len(arr)):
            arr[i] = arr[i][1] - arr[i][0] + 1

        return arr

# even better solution (neetcodes)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        res = []
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0
        return res