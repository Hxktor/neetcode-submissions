class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      seen = set() # hashset to keep track of duplicates 
      for num in nums:
        if num in seen:
          return True
        else:
          seen.add(num)
      return False 
 