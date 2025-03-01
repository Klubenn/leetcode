"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 10^4
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        increm = 0
        i = 1
        res = ""
        while i <= len(a) or i <= len(b):
            sum = increm
            if i <= len(a):
                sum += int(a[-i])
            if i <= len(b):
                sum += int(b[-i])
            increm = sum // 2
            res += str(sum % 2)
            i += 1
        if increm:
            res += str(increm)
        return res[::-1]

print(Solution().addBinary('11', '1'))
print(Solution().addBinary('10', '1'))
print(Solution().addBinary('1010', '1011'))
print(Solution().addBinary('0', '0'))