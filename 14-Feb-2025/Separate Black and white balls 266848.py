# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        steps = left = right = 0
        for right in range(len(s)):
            if s[right] == "0":
                steps += right - left
                left+=1
        return steps