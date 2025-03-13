# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverse(s):
            left, right = 0, len(s)-1
            ans = [0] * len(s)
            while left <= right:
                _left = '1' if s[left] == '0' else '0'
                _right = '1' if s[right] == '0' else '0'
                ans[right] = _left
                ans[left] = _right
                left += 1
                right -= 1
            return ''.join(ans)

        def recursion(k, cur):
            if len(cur) >= k:
                return cur[k-1]
            
            val = cur + '1' + reverse(cur)
            return recursion(k, val)
        return recursion(k, "0")