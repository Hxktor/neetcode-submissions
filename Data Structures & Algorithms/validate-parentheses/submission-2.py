class Solution:
    def isValid(self, s: str) -> bool:
        # create stack to hold s chars
        stack = []
        # check each char in s 
        for c in s:
            if c == ']': # if ] closing check if open matches 
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif c == '}': # closing check if open matches
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif c == ')': # check if closing matches
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack