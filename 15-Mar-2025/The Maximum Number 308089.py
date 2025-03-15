# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m1,m2,m3 = -inf,-inf,-inf

        for i in nums:
            if i > m1:
                m1,m2,m3 = i,m1,m2

            if i < m1 and i > m2:
                m2,m3 = i,m2

            if i < m2 and i > m3:
                m3 = i

        if m1 != m2 and m2 != m3 and m3 != m1 and m1 > -inf and m2 > -inf and m3 > -inf:
            return m3
        else:
            return m1