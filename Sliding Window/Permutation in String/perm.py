class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = Counter(s1)
        l = 0

        for r in range(len(s1),len(s2)+1):
            if s == Counter(s2[l:r]):
                return True
            print(s2[l:r])
            l += 1
        return False


# Not my solution - more optimized
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        
        if n1 > n2: return False

        s1Count = [0] * 26
        s2Count = [0] * 26
        
        # initial values for first set of window
        for i in range(n1):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        for i in range(n2-n1):               # n2-n1 is the number of slides
            if s1Count == s2Count:
                return True
            
            # reduce leaving char count
            s2Count[ord(s2[i]) - ord('a')] -= 1
            
            # increase introduced char count
            s2Count[ord(s2[i+n1]) - ord('a')] += 1

        return s1Count == s2Count    