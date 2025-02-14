# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        validate, left = {}, 0
        for i in range(len(s2)):
            if not s2[i] in s1_counter:
                validate = {}
                left = i+1
                continue
            validate[s2[i]] = validate.get(s2[i], 0) + 1
            if validate == s1_counter:
                return True
        
            while validate[s2[i]] > s1_counter[s2[i]]:
                validate[s2[left]]-=1
                if validate[s2[left]] == 0:
                    validate.pop(s2[left])
                left += 1

        return False