# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = float("-inf")
        for wealth in accounts:
            max_wealth = max(max_wealth, sum(wealth))
        return max_wealth