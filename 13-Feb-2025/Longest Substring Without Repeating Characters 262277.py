# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        initial = 0
        max_length = 0
        for i in range(len(s)):
            if s[i] in char_index:
                initial = initial if initial > char_index[s[i]] + 1 else char_index[s[i]] + 1
                print(initial)
            char_index[s[i]] = i
            max_length = max(max_length, i-initial+1)
        return max_length