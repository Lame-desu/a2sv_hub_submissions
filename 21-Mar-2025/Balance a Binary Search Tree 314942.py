# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def inorder(root):
            nonlocal arr
            if not root:
                return
            
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        inorder(root)

        def sortArray(i, j):
            if i > j:
                return None

            mid = (i + j) // 2
            node = TreeNode(arr[mid])
            node.left = sortArray(i, mid-1)
            node.right = sortArray(mid+1, j)

            return node
        return sortArray(0, len(arr)-1)