# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def recursion(n, k, change):
            if k == 1:
                return '0' if change % 2 == 0 else '1'

            if k == (2 ** n - 1)//2 + 1:
                return '1' if change % 2 == 0 else '0'

            if k < (2 ** n - 1)//2 + 1:
                return recursion(n-1, k, change)
            
            if k > (2 ** n - 1)//2 + 1:
                return recursion(n-1, (2 ** n - 1)-k+1, change+1)
        return recursion(n, k, 0)