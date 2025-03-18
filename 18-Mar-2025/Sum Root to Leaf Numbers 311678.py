# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0 
        def findPathSum(node, value):
            nonlocal res
            value = value * 10 + node.val
            if not node.right and not node.left:
                res += value
                return
            if node.right:
                findPathSum(node.right, value)
            
            if node.left:
                findPathSum(node.left, value)
        findPathSum(root, 0)
        return res