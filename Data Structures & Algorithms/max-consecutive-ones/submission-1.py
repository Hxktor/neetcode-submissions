class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # given an array of 0 and 1's 
        # return Max_consecutive of 1s in array 
        max_count = 0 
        current_count = 0 

        for num in nums:
            if num == 1: 
                current_count += 1 
                if current_count > max_count:
                    max_count = current_count
            else:
                current_count = 0 
        return max_count


     