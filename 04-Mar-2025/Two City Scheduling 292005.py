# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x : x[0] - x[1], reverse = True)
        cost = 0
        i , j = 0, len(costs) - 1
        while i < j:
            cost += costs[j][0]
            cost += costs[i][1]
            i, j = i+1, j-1
      
        return cost