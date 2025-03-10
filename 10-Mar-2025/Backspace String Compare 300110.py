# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s)-1, len(t)-1
        count_s = count_t = 0
        while i > -1 and j > -1:
            if count_s == 0 and count_t == 0 and s[i] != '#' and t[j] != '#':
                if s[i] != t[j]:
                    return False
                i -= 1
                j -= 1
            
            while i > -1 and (count_s > 0 or s[i] == '#'):
                if s[i] == '#':
                    count_s += 1
                else:
                    count_s -= 1
                i -= 1
            
            while j > -1 and (count_t > 0 or t[j] == '#'):
                if t[j] == '#':
                    count_t += 1
                else:
                    count_t -= 1
                j -= 1
        if i == j:
            return True
        return False