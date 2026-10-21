class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack to hold numbers once we see operator we add both of them 
        

        stack  = []
        operators = ['+', '-', '/', '*']
        for token in tokens:
            # if it is one of those operators check 
            if token in operators:
                b = stack.pop() # use stack.pop() bc can have multiple nums
                a = stack.pop() # in our stack
                if token == '+':
                    stack.append(int(a + b))
                
                elif token == '-':
                    stack.append(int(a -b))


                elif token == '*':
                    stack.append(int(a*b))

                else:
                    stack.append(int(a / b))
               # not an operator add to stack     
            else:
                stack.append(int(token))
        return stack[-1] # return output not stack list 
            
        
        