class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left , right ptr 
        left, right = 0 , len(nums) - 1 
        # search for target 
        # sorted in ascending order 

        while left <= right:
            mid = (left + right) // 2 # set midpoint
            if target > nums[mid]: 
                left = mid + 1 
                
            elif target < nums[mid]:
                right = mid - 1
            else: 
                return mid
        return - 1 
        