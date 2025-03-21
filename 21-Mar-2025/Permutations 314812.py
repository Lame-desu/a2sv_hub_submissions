# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        permutation = []

        def backtrack():
            if len(permutation) == len(nums):
                answer.append(permutation[:])
                return

            for i in range(len(nums)):
                if nums[i] not in permutation:
                    permutation.append(nums[i])
                    backtrack()
                    permutation.pop()
        backtrack()
        return answer