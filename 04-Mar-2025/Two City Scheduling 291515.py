# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x : abs(x[0] - x[1]), reverse = True)
        cost = 0
        count_a, count_b, half = 0, 0, len(costs) // 2
        i = 0
        while count_a < half and count_b < half:
            cost += min(costs[i])
            if costs[i][0] <= costs[i][1]:
                count_a += 1
            else:
                count_b += 1
            i += 1
        
        while count_a < half:
            cost += costs[i][0]
            count_a += 1
            i += 1

        while count_b < half:
            cost += costs[i][1]
            count_b += 1
            i += 1

        
        return cost