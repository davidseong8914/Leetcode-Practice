class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()

                if i == "+":
                    stack.append(a + b)
                elif i == "-":
                    stack.append(a - b)
                elif i == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(float(a) / b))
        
        return stack[0]

        