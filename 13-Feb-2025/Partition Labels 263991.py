# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {element: index for index, element in enumerate(s)}

        i, last = 0, len(s) - 1
        ans = []
        while i <= last:
            end, j = last_index[s[i]], i+1 
            while j < end:
                if last_index[s[j]] > end:
                    end = last_index[s[j]]
                j+=1
            ans.append(end - i + 1)
            i = end + 1
        return ans
            
