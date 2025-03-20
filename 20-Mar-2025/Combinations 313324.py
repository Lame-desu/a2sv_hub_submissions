# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        ans = []
        def backtrack(start):
            nonlocal path
            nonlocal ans
            nonlocal n
            if len(path) == k:
                ans.append(copy.deepcopy(path))
                return

            for i in range(start+1, n+1):
                path.append(i)
                backtrack(i)
                path.pop()
        
        backtrack(0)
        return ans  
