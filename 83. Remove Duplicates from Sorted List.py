"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node:
            if node.next:
                if node.next.val == node.val:
                    node.next = node.next.next
                else:
                    node = node.next
            else:
                break
        return head
    

def create_list_sequence(numbers: list) -> Optional[ListNode]:
    if numbers:
        return ListNode(numbers[0], next=(create_list_sequence(numbers[1:]) if len(numbers) >  1 else None))
    return


res = Solution().deleteDuplicates(create_list_sequence([1,1,2,3,4,4,4,4,5]))

while res:
    print(res.val, end=' ')
    res = res.next
print()