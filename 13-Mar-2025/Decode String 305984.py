# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        current_string = ''
        num = ''
        stack = []

        for char in s:
            if 48 <= ord(char) <= 57:
                num += char

            elif char == '[':
                stack.append([current_string, int(num)])
                num = ''
                current_string = ''

            elif char == ']':
                last_string, count = stack.pop()
                current_string =  last_string + count * current_string

            else:
                current_string += char

        return current_string