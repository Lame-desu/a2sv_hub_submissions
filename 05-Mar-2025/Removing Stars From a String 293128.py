# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, s: str) -> str:
        answer = []
        for char in s:
            if char == "*":
                answer.pop()
            else:
                answer.append(char)
        return "".join(answer)