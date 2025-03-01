"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, val in enumerate(nums):
            if target <= val:
                return i
        return i + 1


print(Solution().searchInsert(nums = [1,3,5,6], target = 0))  # 0
print(Solution().searchInsert(nums = [1,3,5,6], target = 5))  # 2
print(Solution().searchInsert(nums = [1,3,5,6], target = 2))  # 1
print(Solution().searchInsert(nums = [1,3,5,6], target = 7))  # 4
print(Solution().searchInsert(nums = [1,3], target = 2))  # 1
print(Solution().searchInsert(nums = [1,3,5], target = 4))  # 2
print(Solution().searchInsert(nums = [3,5,7,9,10], target = 8))  # 3