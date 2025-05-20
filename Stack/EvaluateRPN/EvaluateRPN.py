class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-" :
                stack.append(-(stack.pop()) + stack.pop())
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                temp1 = stack.pop()
                temp2 = stack.pop()
                stack.append(int(float(temp2) / temp1))
            else:
                stack.append(int(c))
        return stack[0]