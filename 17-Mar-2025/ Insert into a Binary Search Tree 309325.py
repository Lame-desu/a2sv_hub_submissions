# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
            
        traverse = root
        while (val < traverse.val and traverse.left) or (val > traverse.val and traverse.right):
            traverse = traverse.right if val > traverse.val else traverse.left
        if val > traverse.val:
            traverse.right = TreeNode(val)
        else:
            traverse.left = TreeNode(val)
        return root