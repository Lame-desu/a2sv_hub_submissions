# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        char_count = Counter(word)
        for char in set(word):
            char_count[char] -= 1
            if char_count[char] == 0:
                char_count.pop(char)
            
            if len(set(char_count.values())) == 1:
                return True

            char_count[char] = char_count.get(char, 0) + 1
        return False