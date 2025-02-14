# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        top_bound = math.floor(math.sqrt(c))
        for i in range(top_bound+1):
            required = math.sqrt(c - (i**2))
            if required == int(required):
                return True
        return False