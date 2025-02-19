# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_array = [0] * len(s)

        for interval in shifts:
            increament = -1 if interval[2] == 0 else 1
            prefix_array[interval[0]] += increament
            if interval[1] < len(s) - 1:
                prefix_array[interval[1] + 1] -= increament
        for i in range(1, len(prefix_array)):
            prefix_array[i] += prefix_array[i-1]
        
        answer = [""] * len(s)
        for index, char in enumerate(s):
            shift_char = chr((ord(char) - ord("a") + prefix_array[index]) % 26 + ord("a"))
            answer[index] = shift_char
        
        return "".join(answer)
