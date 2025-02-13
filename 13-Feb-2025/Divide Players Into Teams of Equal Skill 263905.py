# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i, j = 0, len(skill) - 1
        total_skill = skill[i] + skill[j]
        teams_chemistry = 0
        while i < j:
            current_skill = skill[i] + skill[j]
            if current_skill != total_skill:
                return -1
            teams_chemistry += skill[i] * skill[j]
            i, j = i+1, j-1
        return teams_chemistry