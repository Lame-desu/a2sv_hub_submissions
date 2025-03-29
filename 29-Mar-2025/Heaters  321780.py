# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        def validate_r(r):
            i, j = 0, 0

            while i < len(houses) and j < len(heaters):
                if abs(houses[i] - heaters[j]) <= r:
                    i += 1
                elif houses[i] >= heaters[j]:
                    j += 1
                else:
                    return False
            return i == len(houses)

        heaters.sort()
        houses.sort()
        
        min_r, max_r = 0, max(abs(heaters[0] - houses[0]), abs(heaters[0] - houses[-1]))

        while min_r <= max_r:
            mid = (min_r + max_r) // 2

            if validate_r(mid):
                max_r = mid - 1
            else:
                min_r = mid + 1

        return min_r 