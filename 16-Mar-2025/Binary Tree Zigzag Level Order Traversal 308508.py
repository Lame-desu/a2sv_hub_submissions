# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        arr = [root]
        result = []
        while arr:
            result.append(arr)
            arr = []
            for i in range(len(result[-1])-1, -1, -1):
                
                right_val = result[-1][i].right
                left_val = result[-1][i].left
                if right_val and len(result) % 2 == 1:
                    arr.append(right_val)
                if left_val and len(result) % 2 == 1:
                    arr.append(left_val)

                if left_val and len(result) % 2 == 0:
                    arr.append(left_val)
                if right_val and len(result) % 2 == 0:
                    arr.append(right_val)

        for array in result:
            for i in range(len(array)):
                array[i] = array[i].val
        return result

                