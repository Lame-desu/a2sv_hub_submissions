# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def backtrack(num):
            if len(path) == k:
                ans.append(path[:])
                return
            
            if num >= n:
                return
            
            path.append(num+1)
            backtrack(num+1)
            path.pop()
            backtrack(num+1)

        backtrack(0)
        return ans

