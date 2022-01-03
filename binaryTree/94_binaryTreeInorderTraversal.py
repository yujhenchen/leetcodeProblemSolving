from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        if root != None:
            result.extend((self.inorderTraversal(root.left)))
            result.append(root.val)
            # print(root.val)
            result.extend((self.inorderTraversal(root.right)))
        return result
