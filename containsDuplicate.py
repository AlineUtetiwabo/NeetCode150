# Given an integer array nums, return true if any value appears more than once in the array, 
# otherwise return false.
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        for i in nums:
            if i in seen:
                return True
            else:
                seen.append(i)
            print(i)
        return False  
    
# create an instance of the Solution class
solution = Solution()

# call the hasDuplicate with an array
result = solution.hasDuplicate([1, 1, 2, 3, 4])