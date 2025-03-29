# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        def validate_m(mid):
            count = 1
            initial = position[0]
            for i in range(1, len(position)):
                if position[i] - initial >= mid:
                    initial = position[i]
                    count += 1
                
                if count >= m:
                    return True
            return False



        position.sort()
        min_m, max_m = 1, position[-1] - position[0]

        while min_m <= max_m:
            mid = (min_m + max_m) // 2

            if validate_m(mid):
                min_m = mid + 1
            else:
                max_m = mid - 1
        return max_m