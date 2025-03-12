# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_queue = deque()
        max_queue = deque()

        left = ans = 0
        for right, num in enumerate(nums):

            while min_queue and num < min_queue[-1]:
                min_queue.pop()
            min_queue.append(num)
            
            while max_queue and num > max_queue[-1]:
                max_queue.pop()
            max_queue.append(num)

            while max_queue[0] - min_queue[0] > limit:
                if nums[left] == min_queue[0]:
                    min_queue.popleft()
                
                if nums[left] == max_queue[0]:
                    max_queue.popleft()

                left += 1

            ans = max(ans, right - left + 1)
        return ans