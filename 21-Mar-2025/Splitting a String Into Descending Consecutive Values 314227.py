# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        
        def backtrack(index, prevValue, count):

            if index >= len(s):
                return count >= 2


            for i in range(index+1, len(s)+1):
                currentValue = int(s[index: i])
                if count == 0:
                    if backtrack(i, currentValue, count+1):
                        return True

                elif prevValue - currentValue == 1:
                    if backtrack(i, currentValue, count+1):
                        return True
                    
                elif prevValue - currentValue <= 0:
                    return False

            return False
        return backtrack(0, None, 0)
