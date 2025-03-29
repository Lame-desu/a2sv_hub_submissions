# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # first search in the column
        initial, final = 0, len(matrix)-1
        
        while initial <= final:
            mid = (initial + final) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                final -= 1
            else:
                initial += 1

        if final < 0:
            return False
        
        c_initial, c_final = 0, len(matrix[0])-1
        
        while c_initial <= c_final:
            mid = (c_initial + c_final) // 2
            if matrix[final][mid] == target:
                return True
            elif matrix[final][mid] > target:
                c_final = mid - 1
            else:
                c_initial = mid + 1
        return False
