# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverseOdd(left, right, level):
            if not left or not right:
                return
            
            if level % 2 == 1:
                tempo = left.val
                left.val = right.val
                right.val = tempo
            reverseOdd(left.left, right.right, level+1)
            reverseOdd(left.right, right.left, level+1)

        reverseOdd(root.left, root.right, 1)
        return root