# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        _rs = 0
        _ls = 0
        for char in s:
            if char == "R":
                _rs += 1
            elif char == "L":
                _ls += 1

            if _rs == _ls:
                count += 1
        return count