# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        def backtrack(string):
            if len(string) == n:
                ans.append(string)
                return

            if not string or string[-1] == '1':
                backtrack(string + "0")
            
            backtrack(string + "1")
        backtrack("")
        return ans