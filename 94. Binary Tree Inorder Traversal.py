"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]

Output: [1,3,2]

Explanation:



Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,2,6,5,7,1,3,9,8]

Explanation:



Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]

 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, res = [], []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res
        
        
        res = []
        if not root:
            return res
        stack = [root]
        while(stack):
            if stack[-1].left not in res:
                while stack[-1].left:
                    stack.append(stack[-1].left)
            node = stack.pop()
            res.append(node)
            if node.right:
                stack.append(node.right)
        return [r.val for r in res]
    

root = TreeNode(2, left=TreeNode(3, TreeNode(1)), right=None)
print(Solution().inorderTraversal(root))

root = TreeNode(val=3, left=TreeNode(val=1, left=None, right=TreeNode(val=2, left=None, right=None)), right=None)
print(Solution().inorderTraversal(root))




        

            
