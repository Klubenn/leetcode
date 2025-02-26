"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {value: index for index, value in enumerate(nums)}
        for i in range(len(nums)):
            search_value = target - nums[i]
            index = hash_table.get(search_value, None)
            if index is not None and index != i:
                return [index, i]
            
        # slow solution
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
                
print(Solution().twoSum([2,7,11,15], 9))  # [0,1]
print(Solution().twoSum([3,2,4], 6))  # [1,2]
print(Solution().twoSum([3,3], 6))  # [0,1]