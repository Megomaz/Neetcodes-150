class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            key = tuple(sorted(word))
            if key in hashmap:
               hashmap[key].append(word)
            else:
                hashmap[key] = [word]

        return hashmap.values()