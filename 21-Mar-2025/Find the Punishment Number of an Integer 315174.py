# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def backtrack(index, initial, squared, num):
            if index >= len(squared):
                return num == initial

            for i in range(index+1, len(squared)+1):
                value = int(squared[index:i]) + initial
                if value > num:
                    return False

                if backtrack(i, value, squared, num):
                    return True

            return False
        sum = 0
        for num in range(1, n+1):
            if backtrack(0, 0, str(num**2), num):
                sum += num**2

        return sum

