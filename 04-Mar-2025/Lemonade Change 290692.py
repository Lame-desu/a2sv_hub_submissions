# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for payment in bills:
            if payment == 5:
                fives += 1

            elif payment == 10:
                if fives > 0:
                    fives -= 1
                    tens += 1
                else:
                    return False

            else:
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                elif fives > 2:
                    fives -= 3
                else:
                    return False
        return True