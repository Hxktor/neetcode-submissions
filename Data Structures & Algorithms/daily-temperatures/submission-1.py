class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures) # return answer result 
        stack = [] # keep track of the temperature and the index 
        
        for index , temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackInd = stack.pop()
                answer[stackInd] = index - stackInd
            stack.append((temp,index))
        return answer