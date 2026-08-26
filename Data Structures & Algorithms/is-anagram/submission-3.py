
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # if length do not match return false  
            return False 
        
        # charchater is key value is count 
        # keep count of each string 
        #return true if countT and countS == eachother 

        countT , countS = {} , {}

        for c in s:
            countS[c] = countS.get(c, 0) + 1 
        for c in t:
            countT[c] = countT.get(c , 0) + 1 
        return countT == countS