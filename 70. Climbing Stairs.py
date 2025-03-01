"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 
4 steps:
1 + 1 + 1 + 1
1 + 1 + 2
1 + 2 + 1
2 + 1 + 1
2 + 2

5 steps:
1 + 1 + 1 + 1 + 1
1 + 1 + 1 + 2
1 + 1 + 2 + 1
1 + 2 + 1 + 1
2 + 1 + 1 + 1
2 + 2 + 1
2 + 1 + 2
1 + 2 + 2

6 steps:
1 + 1 + 1 + 1 + 1 + 1
1 + 1 + 1 + 1 + 2
1 + 1 + 1 + 2 + 1
1 + 1 + 2 + 1 + 1
1 + 2 + 1 + 1 + 1
2 + 1 + 1 + 1 + 1
1 + 2 + 2 + 1
1 + 2 + 1 + 2
1 + 1 + 2 + 2
2 + 1 + 1 + 2
2 + 2 + 1 + 1
2 + 1 + 2 + 1
2 + 2 + 2

Constraints:

1 <= n <= 45
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        res = 1
        prev = 0
        for i in range(1, n + 1):
            prev_prev = prev
            prev = res
            res = prev + prev_prev
        return res


        if n == 1 or n == 2:
            return n
        return self.climbStairs(n - 2) + self.climbStairs(n - 1)
    
print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
print(Solution().climbStairs(4))
print(Solution().climbStairs(5))
print(Solution().climbStairs(6))
print(Solution().climbStairs(44))