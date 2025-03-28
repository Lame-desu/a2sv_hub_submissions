# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        def canGet(val):
            childs_got = 0
            for num in candies:
                childs_got += (num // val)
                if childs_got >= k:
                    return True
            return False

        min_val, max_val = 1, max(candies)
        while min_val <= max_val:
            mid = (min_val + max_val) // 2
            if canGet(mid):
                min_val = mid + 1
            else:
                max_val = mid - 1

        return max_val