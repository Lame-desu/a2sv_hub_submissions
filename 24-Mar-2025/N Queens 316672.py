# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        valid_position = []
        answer = []
        column, diagonal, s_diagonal = set(), set(), set()
        def backtrack(r):
            if r == n:
                answer.append(valid_position[:])
                return


            for i in range(n):
                if i in column or i - r in diagonal or i + r in s_diagonal:
                    continue
                column.add(i), diagonal.add(i-r), s_diagonal.add(i+r)

                valid_position.append("." * i + "Q" + (n-i-1) * ".")
                backtrack(r+1)

                column.remove(i), diagonal.remove(i-r), s_diagonal.remove(i+r)
                valid_position.pop()  
        backtrack(0)
        return answer            

            