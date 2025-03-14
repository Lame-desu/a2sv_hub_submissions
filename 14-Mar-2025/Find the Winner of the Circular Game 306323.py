# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        array = [i for i in range(1, n+1)]
        current = 0
        while len(array) > 1:
            next_remove = (current + k - 1) % len(array)
            array.pop(next_remove)
            current = next_remove
        return array[0]