# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def sortArray(i, j):
            if i > j:
                return None

            mid = (i + j) // 2
            node = TreeNode(nums[mid])
            node.left = sortArray(i, mid-1)
            node.right = sortArray(mid+1, j)

            return node
        return sortArray(0, len(nums)-1)