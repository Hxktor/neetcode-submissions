class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indicies = {} # setting value -> index 
        # i = index n = number 
        for i, n in enumerate(nums):
            diff = target - n 
            if diff in indicies:
                return [indicies[diff], i]
            indicies[n] = i