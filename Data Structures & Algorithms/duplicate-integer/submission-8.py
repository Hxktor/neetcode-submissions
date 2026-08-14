class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force compare each pair if num [i] == num[j]
        # return true else false
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False
