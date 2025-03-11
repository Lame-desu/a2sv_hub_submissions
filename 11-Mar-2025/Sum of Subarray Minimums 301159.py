# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        left = [-1] * len(arr)
        right = [len(arr)] * len(arr)
        stack = []

        for i, num in enumerate(arr):
            while stack and num < arr[stack[-1]]:
                stack.pop()
            left[i] = -1 if not stack else stack[-1]
            stack.append(i)


        stack = []
        for i in range(len(arr)-1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            right[i] = len(arr) if not stack else stack[-1]
            stack.append(i)

        return sum([((i-left[i]) * (right[i] - i) * arr[i]) for i in range(len(arr))]) % (10 ** 9 + 7)