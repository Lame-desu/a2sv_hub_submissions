# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        char_set = {}
        for char in s:
            char_set[char] = char_set.get(char, 0) + 1
        value = char_set[s[0]]
        for char, frequency in char_set.items():
            if frequency != value:
                return False
        return True
