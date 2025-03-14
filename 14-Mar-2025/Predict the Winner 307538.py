# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        store_duplicate = {}
        def maximize_score(i, j):
            if (i, j) in store_duplicate:
                return store_duplicate[(i, j)]

            if i > j:
                return 0

            alternative_1 = nums[i] + min(maximize_score(i+1, j-1), maximize_score(i+2, j))
            alternative_2 = nums[j] + min(maximize_score(i, j-2), maximize_score(i+1, j-1))

            score = max(alternative_1, alternative_2)

            store_duplicate[(i, j)] = score

            return score

        player1 = maximize_score(0, len(nums)-1)
        return player1 >= sum(nums) - player1