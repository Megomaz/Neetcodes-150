class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""

        values = self.hashmap[key]

        l,r = 0, len(values) - 1
        res = ""  # default if no valid timestamp

        while l <= r:
            mid = ((l + r) // 2)
            if values[mid][0] <= timestamp:
                res = values[mid][1] # valid candidate
                l = mid + 1 # try to find a later one
            else:
                r = mid - 1

        return res
