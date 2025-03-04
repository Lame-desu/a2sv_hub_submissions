# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        _ones = s.count("1")
        return (_ones - 1) * "1" + (len(s) - (_ones)) * "0" + "1"