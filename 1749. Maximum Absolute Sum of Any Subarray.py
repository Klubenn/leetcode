"""
You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.
 

Example 1:

Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
Example 2:

Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.
"""

from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        cumulative = [nums[0]]
        for i in range(1, len(nums)):
            cumulative.append(cumulative[-1] + nums[i])
        max_cum = max(cumulative)
        min_cum = min(cumulative)
        
        if max_cum * min_cum > 0:
            return max(abs(max_cum), abs(min_cum))
        else:
            return abs(max_cum - min_cum)

print(Solution().maxAbsoluteSum([1, -3, 2, 3, -4]))  # 5
print(Solution().maxAbsoluteSum([2, -5, 1, -4, 3, -2]))  # 8
print(Solution().maxAbsoluteSum([1, 2, 3]))  # 6
print(Solution().maxAbsoluteSum([-1, -2, -3]))  # 6
print(Solution().maxAbsoluteSum([5]))  # 5
print(Solution().maxAbsoluteSum([-5]))  # 5