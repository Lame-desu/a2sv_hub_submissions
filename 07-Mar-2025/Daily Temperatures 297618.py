# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)-1, -1, -1):

            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            value = 0 if not stack else stack[-1][1] - i
            answer[i] = value
            stack.append([temperatures[i], i])
        return answer