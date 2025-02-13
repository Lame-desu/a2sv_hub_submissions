# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums)
        return nums

    def merge_sort(self, arry):
        if len(arry) == 1:
            return

        mid_point = len(arry) // 2
        arr1 = arry[:mid_point]
        arr2 = arry[mid_point:]
        self.merge_sort(arr1)
        self.merge_sort(arr2)
        self.sort(arr1, arr2, arry)
    def sort(self, arr1, arr2, arry):
        i, j, k = 0, 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                arry[k] = arr1[i]
                i, k = i+1, k+1
            else:
                arry[k] = arr2[j]
                j, k = j+1, k+1

        while i < len(arr1):
            arry[k] = arr1[i]
            i, k = i+1, k+1
        while j < len(arr2):
            arry[k] = arr2[j]
            j, k = j+1, k+1
