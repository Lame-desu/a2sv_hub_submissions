# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        i = answer = 0
        stack = []
        while i < len(s):
            if s[i] == '(':
                stack.append(s[i])
                i += 1
                continue
            count = -1
            while i < len(s) and s[i] == ')':
                stack.pop()
                count += 1
                i += 1
            answer += (2 ** count) * (2 ** len(stack))
        return answer