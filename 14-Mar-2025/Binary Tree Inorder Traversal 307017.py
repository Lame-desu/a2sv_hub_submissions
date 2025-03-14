# Problem: Binary Tree Inorder Traversal - https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def recursive(answer, root):
            if not root:
                return answer

            recursive(answer, root.left)
            answer.append(root.val)
            recursive(answer, root.right)
            return answer

        return recursive([], root)