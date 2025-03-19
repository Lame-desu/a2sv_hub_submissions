# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        answer = 0
        def findAverage(node):
            nonlocal answer
            if not node:
                return [0, 0]

            right = findAverage(node.right)
            left = findAverage(node.left)
            _sum, count = right[0] + left[0] + node.val, right[1] + left[1] + 1
            if _sum // count == node.val:
                answer += 1
            return [_sum, count]    
        findAverage(root)
        return answer 

    