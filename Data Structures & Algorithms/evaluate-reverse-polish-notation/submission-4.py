class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # initialize stack to keep track of integers to +,-,*,/
        stack = []
        # go over eack character in string tokens
        for c in tokens:
            # check if c is one of the operators
            # tokens=["2","1","+","3","*"]
            # [2, 1] + 
            # b^ a^ b + a = 3 
            # [3, 3, ] * 
             #b^  a^ 3*3 = 9 
             #stack [9]
             # return stack[0]
            if c in "+-*/":

                a = stack.pop()
                b = stack.pop()
                if c == "+":
                    stack.append(b + a)
                elif c == "-":
                    stack.append(b - a)

                elif c == "*":
                    stack.append(b * a)

                else:
                    stack.append(int(b / a))
            
            
            else: 
                stack.append(int(c))
        return stack[0]