# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        answer = []
        opperations = {'+', '-', '*', '/'}
        for opperand in tokens:
            if opperand in opperations:
                opp2 = answer.pop()
                opp1 = answer.pop()
                val = str(int(eval(opp1 + opperand + opp2)))
                print(val)
                answer.append(val)
            else:
                answer.append(opperand)
        return int(answer[0])
