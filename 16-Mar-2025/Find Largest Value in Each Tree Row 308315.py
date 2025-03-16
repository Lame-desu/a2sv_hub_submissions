# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        count = 1
        next_count = 0
        maximum = float('-inf')
        result = []
        while queue:
            node = queue.popleft()
            count -= 1
            maximum = max(maximum, node.val)

            if node.left:
                queue.append(node.left)
                next_count += 1

            if node.right:
                queue.append(node.right)
                next_count += 1

            if count == 0:
                result.append(maximum)
                count = next_count
                next_count = 0
                maximum = float("-inf")
            
        return result