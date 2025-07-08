class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []

        for index,char in enumerate(s):
            if char == '(':
                left.append(index)
            elif char == '*':
                star.append(index)
            else:
                if not left and not star: # if we see ')' and dont have a '(' or '*' return false immediately
                    return False
                elif left:
                    left.pop()
                else:
                    star.pop()


        while left and star:
            if left.pop() > star.pop(): # check if we have any unmatched left parenthesis that we cant deal with e.g. s = "(*("
                return False
        return not left
