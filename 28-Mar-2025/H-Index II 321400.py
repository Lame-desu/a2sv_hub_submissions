# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        i, j = 0, len(citations)-1
        max_h = float('-inf')
        while i <= j:
            mid = (i + j) // 2
            if citations[mid] >= len(citations) - mid:
                max_h = max(max_h, len(citations) - mid)
                j = mid - 1
            else:
                max_h = max(max_h, citations[mid])
                i = mid + 1
        return max_h