class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # array of nums and int val = k 
        # so if val in nums, remove num 
        k = 0 
        for num in nums:
            if num != val:
                nums[k] = num  
                k += 1
        return k

