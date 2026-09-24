class Solution:
    def isPalindrome(self, s: str) -> bool:
        l , r = 0 , len(s) - 1 # initalize left and right pointers 
        while l < r: 
            # skip non alpha numeric characters from left 
            while l < r and not s[l].isalnum():
                l += 1
            # skip non alphanumeric characters from right
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1 
            r -= 1 
        return True 

        



    

       

        
        
        