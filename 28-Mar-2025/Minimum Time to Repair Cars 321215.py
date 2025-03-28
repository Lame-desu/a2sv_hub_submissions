# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def canRepair(minuite):
            repaired_cars = 0
            for rank in ranks:
                repaired_cars += math.floor((minuite / rank) ** 0.5)
                if repaired_cars >= cars:
                    return True
            return repaired_cars >= cars

        min_min, max_min = 0, max(ranks) * (cars ** 2)
        while min_min <= max_min:
            mid = (min_min + max_min) // 2
            if canRepair(mid):
                max_min = mid - 1
            else:
                min_min = mid + 1
        return min_min