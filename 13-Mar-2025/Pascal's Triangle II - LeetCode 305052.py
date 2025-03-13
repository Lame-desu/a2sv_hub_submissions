# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        answer = [1]
        for i in range(rowIndex):
            for i in range(len(answer)-1, 0, -1):
                answer[i]+=answer[i-1]
            answer.append(1)
        return answer
            
        