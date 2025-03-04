# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits = 0
        remainings = {}
        for answer in answers:
            if answer == 0:
                rabbits += 1
            elif answer in remainings:
                remainings[answer] -= 1
                if remainings[answer] == 0:
                    del remainings[answer]
            else:
                rabbits += answer + 1
                remainings[answer] = answer
        return rabbits