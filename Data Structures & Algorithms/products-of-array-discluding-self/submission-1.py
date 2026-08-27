class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
    
        # 1. Pass Left to Right (Build Prefix)
        prefix_total = 1
        for i in range(n):
            res[i] = prefix_total
            prefix_total *= nums[i]
        
        # 2. Pass Right to Left (Multiply by Postfix)
        postfix_total = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix_total
            postfix_total *= nums[i]
        
        return res