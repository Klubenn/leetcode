"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 2^31 - 1
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        start, end = 1, x
        while start <= end:
            check = (end - start) // 2 + start
            if check == x // check:
                return check
            if check > x // check:
                end = check - 1
            else:
                start = check + 1
        return end


        if x <= 1:
            return x
        i = 1
        counter = 1
        reduced = x
        while reduced > i:
            reduced -= i
            counter += 1
            i += 2
        return counter if reduced == i else counter - 1
        
        
        i = 0
        while True:
            if i * i > x:
                return i - 1
            if i * i == x:
                return i
            i += 1

print(Solution().mySqrt(4))
print(Solution().mySqrt(8))
print(Solution().mySqrt(64))

"""
64:
64 - 1      | 
63 - 3      |
60 - 5      |
55 - 7      | 8
48 - 9      |
39 - 11     |
28 - 13     |
15 - 15     |
"""