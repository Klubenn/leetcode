"""
Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x) == str(x)[::-1]
        if x < 0:
            return False
        y = x
        reverse = 0
        while y > 0:
            z = y % 10
            reverse = reverse * 10 + z
            y //= 10
        return reverse == x
    
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(121))
print(Solution().isPalindrome(10))
print(Solution().isPalindrome(0))
print(Solution().isPalindrome(101))
print(Solution().isPalindrome(12321))
print(Solution().isPalindrome(123321))
print(Solution().isPalindrome(123421))