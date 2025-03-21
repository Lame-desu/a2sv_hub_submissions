# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        arr = []
        min_num = "999999999"
        def backtrack(index, initial):
            nonlocal min_num
            if index == len(pattern):
                min_num = min(min_num, "".join(arr))
                return

            if "".join(arr) > min_num:
                return

            if not initial:
                x, y = 1, 10
            else:
                if pattern[index] == 'I':
                    x, y = initial+1, 10
                else:
                    x, y = 1, initial

            for i in range(x, y):
                if not str(i) in arr:
                    arr.append(str(i))
                    backtrack(index+1, i)
                    arr.pop()
        backtrack(-1, 0)
        return min_num

