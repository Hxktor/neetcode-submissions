class Solution:
    def trap(self, height: List[int]) -> int:
        # check if array empty if it is return 0 
        if not height:
            return 0
        
        left , right = 0 , len(height) - 1 # left , right ptrs 
        # set a current max and right height 
        leftmax, rightmax = height[left], height[right]
        # set reesult 
        result = 0 
        while left < right: 
            if leftmax < rightmax: 
                left += 1 
                leftmax = max(leftmax, height[left])
                result += leftmax - height[left]
            else: 
                right -= 1 
                rightmax = max(rightmax, height[right])
                result += rightmax - height[right]
        return result 
        