class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        def generate(Open,close):
            if Open + close == n * 2:
                result.append(''.join(stack))
                return

            if Open < n:
                stack.append('(')
                generate(Open + 1,close)
                stack.pop()
            
            if close < Open:
                stack.append(')')
                generate(Open, close+ 1)
                stack.pop()

        generate(0,0)
        return result
            




            
            