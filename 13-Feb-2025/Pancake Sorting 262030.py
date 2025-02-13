# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        answer = []
        for i in range(len(arr)-1, 0, -1):
            if arr[i] == i+1:
                continue
            
            for j in range(i):
                if arr[j] == i+1:
                    self.flip(arr, j)
                    answer.append(j+1)
                    break
            self.flip(arr, i)
            answer.append(i+1)
        return answer

    def flip(self, arr, i):
        initial = 0
        while initial < i:
            arr[initial], arr[i] = arr[i], arr[initial]
            initial, i = initial+1, i-1
        