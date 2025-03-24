# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def backtrack(uncovered, remaining, string):
            if uncovered == remaining == 0:
                answer.append(string)
                return
            
            if uncovered > 0:
                backtrack(uncovered-1, remaining, string + ")" )

            if remaining > 0:
                backtrack(uncovered+1, remaining-1, string + "(")

        backtrack(1, n-1, "(")
        return answer