# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        answer = []
        for word in path:
            if not word or word == ".":
                continue
            elif word == "..":
                if len(answer) > 0:
                    answer.pop()
            else:
                answer.append(word)
        return "/" + "/".join(answer)