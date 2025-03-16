# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def maxDifference(node, arr):
            if not node:
                return abs(arr[0] - arr[1])
            
            if node.val > arr[0]:
                arr[0] = node.val
            
            if node.val < arr[1]:
                arr[1] = node.val

            # print(arr)
            copy_right = copy.deepcopy(arr)
            left = maxDifference(node.left, arr)
            right = maxDifference(node.right, copy_right)
            return max(left, right)
        return maxDifference(root, [float("-inf"), float("inf")])