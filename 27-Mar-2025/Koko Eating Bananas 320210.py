# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def findHours(value):
            hours = 0
            for bananas in piles:
                hours += math.ceil(bananas / value)
                if hours > h:
                    return False
            return True
        # print(findHours(3))
        min_val, max_val = 1, max(piles)
        while min_val <= max_val:
            mid = (min_val + max_val) // 2
            if findHours(mid):
                max_val = mid-1
            else:
                min_val = mid+1
        return max_val + 1