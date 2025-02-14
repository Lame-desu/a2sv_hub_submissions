# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sub_string = Counter(t)
        current = {}
        left = 0
        start_end = [0, len(s) + 5]
        for right in range(len(s)):
            current[s[right]] = current.get(s[right], 0) + 1
            while self.validate(current, sub_string):
                start_end = start_end if start_end[1] - start_end[0] <= right - left else [left, right]
                current[s[left]]-=1
                left+=1
        return "" if start_end[1] - start_end[0] > len(s) else s[start_end[0]: start_end[1]+1]


    def validate(self, current, sub_string):
        for char, freq in sub_string.items():
            if current.get(char, 0) < freq:
                return False
        return True