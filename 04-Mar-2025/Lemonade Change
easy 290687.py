# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = {5 : 0, 10 : 0}
        for payment in bills:
            if payment == 5:
                changes[5] += 1

            elif payment == 10:
                if changes[5] > 0:
                    changes[5] -= 1
                    changes[10] += 1
                else:
                    return False

            else:
                if changes[10] > 0 and changes[5] > 0:
                    changes[10] -= 1
                    changes[5] -= 1
                elif changes[5] > 2:
                    changes[5] -= 3
                else:
                    return False
        return True