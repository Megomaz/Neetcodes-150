class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        result = []

        def backtrack(i,curr):
            if len(curr) == len(digits):
                result.append(curr)
                return

            for letter in hashmap[digits[i]]:
                backtrack(i+1,curr + letter) 


        if digits:
            backtrack(0,"")
        return result

        