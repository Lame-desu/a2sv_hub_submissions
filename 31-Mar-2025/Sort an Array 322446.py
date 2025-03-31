# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.mergeSort(left, right)


    def mergeSort(self, left, right):
        i, j = 0, 0
        answer = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                answer.append(left[i])
                i += 1
            else:
                answer.append(right[j])
                j += 1
        
        answer.extend(left[i:])
        answer.extend(right[j:])
        return answer
