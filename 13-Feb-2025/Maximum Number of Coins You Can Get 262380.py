# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_sum = 0
        left = 0
        right = len(piles) - 2
        while left<right:
            max_sum+=piles[right]
            right-=2
            left+=1
        return max_sum