# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count = 1
        initial = points[0][0]
        final = points[0][1]

        for i, j in points[1:]:
            if i > final:
                count += 1
                initial = i
                final = j
            initial = max(initial, i)
            final = min(final, j)
        return count
                