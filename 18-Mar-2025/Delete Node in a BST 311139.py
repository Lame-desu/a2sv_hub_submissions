# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findNode(val, node):
            if not node:
                return None
            if node.left and node.left.val == key:
                return node
            if node.right and node.right.val == key:
                return node
            if key < node.val:
                return findNode(val, node.left)
            else:
                return findNode(val, node.right)


        def inOrderTraverse(changeVal, toFind):
            if not toFind.left.left:
                changeVal.val = toFind.left.val
                toFind.left = toFind.left.right
                return
            inOrderTraverse(changeVal, toFind.left)
        dummy = TreeNode(float("inf"), left=root)
        toReturn = dummy
        toBeRemoved = findNode(key, dummy)
        # print(toBeRemoved)
        if not toBeRemoved:
            return root
        elif key < toBeRemoved.val:
            if not toBeRemoved.left.left and not toBeRemoved.left.right:
                toBeRemoved.left = None
            elif not toBeRemoved.left.left:
                toBeRemoved.left = toBeRemoved.left.right
            elif not toBeRemoved.left.right:
                toBeRemoved.left = toBeRemoved.left.left
            else:
                if not toBeRemoved.left.right.left:
                    toBeRemoved.left.right.left = toBeRemoved.left.left
                    toBeRemoved.left = toBeRemoved.left.right
                else:
                    inOrderTraverse(toBeRemoved.left, toBeRemoved.left.right)
        elif key > toBeRemoved.val:
            if not toBeRemoved.right.left and not toBeRemoved.right.right:
                toBeRemoved.right = None
            elif not toBeRemoved.right.left:
                toBeRemoved.right = toBeRemoved.right.right
            elif not toBeRemoved.right.right:
                toBeRemoved.right = toBeRemoved.right.left
            else:
                if not toBeRemoved.right.right.left:
                    toBeRemoved.right.right.left = toBeRemoved.right.left
                    toBeRemoved.right = toBeRemoved.right.right
                else:
                    inOrderTraverse(toBeRemoved.right, toBeRemoved.right.right)

        return toReturn.left



                
