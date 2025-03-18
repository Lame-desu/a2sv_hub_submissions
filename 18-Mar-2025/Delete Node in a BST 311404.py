# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findRightMinimum(self, node):
        if not node.left:
            return node
        return self.findRightMinimum(node.left)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == key:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                rightMin = self.findRightMinimum(root.right)
                root.val = rightMin.val
                rightMin.val = key
                root.right = self.deleteNode(root.right, key)
                return root


        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        
        else:
            root.left = self.deleteNode(root.left, key)
            return root