class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(i,curr):
            if i == len(s):
                result.append(curr[:])
                return

            for j in range(i,len(s)):
                if isPalindrome(s,i,j):
                    curr.append(s[i:j+1])
                    backtrack(j+1,curr)
                    curr.pop()

        def isPalindrome(string, l, r):

            while l < r:
                if string[l] != string[r]:
                    return False
                l +=1 
                r -= 1

            return True
        backtrack(0,[])
        return result

           
                