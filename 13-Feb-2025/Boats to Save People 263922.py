# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people) - 1
        count = 0
        while i <= j:
            if people[i] + people[j] <= limit:
                i, j, count = i+1, j-1, count+1
            else:
                j-=1
                count+=1
        return count