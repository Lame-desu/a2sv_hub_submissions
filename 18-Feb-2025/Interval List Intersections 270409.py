# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        answer = []
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            if firstList[i][0] <= secondList[j][1]:
                interval = [max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])]
                if interval[0] <= interval[1]:    
                    answer.append(interval)
                if firstList[i][1] <=secondList[j][1]:
                    i+=1
                else:
                    j+=1
            else:
                j+=1
        return answer