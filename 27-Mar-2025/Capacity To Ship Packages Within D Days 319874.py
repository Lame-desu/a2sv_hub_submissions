# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def findLengthOfDay(value):
            maxDays = 1
            sum = 0
            for weight in weights:
                if sum + weight > value:
                    maxDays += 1
                    sum = weight
                else:
                    sum += weight
            return maxDays
        
        minVal = max(weights)
        maxVal = sum(weights)
        minWeight = maxVal
        while minVal < maxVal:
            mid = (minVal + maxVal) // 2
            if findLengthOfDay(mid) <= days:
                maxVal = minWeight = mid
            else:
                minVal = mid+1
        return minWeight 

