"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:
list1: 1 -> 2 -> 4
list2: 1 -> 3 -> 4
output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sorted_seq = ListNode()
        answer = sorted_seq
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    sorted_seq.next = list1
                    list1 = list1.next
                    sorted_seq = sorted_seq.next
                else:
                    sorted_seq.next = list2
                    list2 = list2.next
                    sorted_seq = sorted_seq.next
            else:
                sorted_seq.next = list2 if list2 else list1
                break
        return answer.next

def create_list_sequence(numbers: list) -> Optional[ListNode]:
    if numbers:
        return ListNode(numbers[0], next=(create_list_sequence(numbers[1:]) if len(numbers) >  1 else None))
    return

arr1 = create_list_sequence([1, 2, 3, 5])
arr11 = create_list_sequence([3, 4, 5])
res1 = Solution().mergeTwoLists(arr1, arr11)

arr2 = create_list_sequence([])
arr22 = create_list_sequence([7,8])
res2 = Solution().mergeTwoLists(arr2, arr22)

arr3 = create_list_sequence([4,5])
arr33 = create_list_sequence([])
res3 = Solution().mergeTwoLists(arr3, arr33)

for res in [res1, res2, res3]:
    while res:
        print(res.val, end=' ')
        res = res.next
    print()
