# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        min_unfairness = float("inf")
        def backtrack(array, index):
            nonlocal min_unfairness
            if index == len(cookies):
                if len(array) == k:
                    min_unfairness = min(min_unfairness, max(array))
                    # print(array)
                return


            for j in range(len(array)):
                new_arr = array[:]
                new_arr[j] += cookies[index]
                backtrack(new_arr, index+1)
            if len(array) < k:
                arr_copy = array[:]
                arr_copy.append(cookies[index])
                backtrack(arr_copy, index+1)

        backtrack([], 0)
        return min_unfairness