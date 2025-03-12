# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

import sys
import itertools
from collections import deque


def input():
    return sys.stdin.readline().strip()

def read_ints():
    return list(map(int, input().split()))

def read_int():
    return int(input())

def read_matrix(rows):
    return [read_ints() for _ in range(rows)]

def run_tests(solve):
    t = read_int()
    for _ in range(t):
        solve()

def solve():
    n, k = read_ints()
    array = read_ints()
    minimums = deque()
    maximums = deque()

    left = ans = 0
    for right in range(n):
        while minimums and array[right] < minimums[-1]:
            minimums.pop()
        minimums.append(array[right])

        while maximums and array[right] > maximums[-1]:
            maximums.pop()
        maximums.append(array[right])

        while maximums[0] - minimums[0] > k:
            if array[left] == maximums[0]:
                maximums.popleft()
            if array[left] == minimums[0]:
                minimums.popleft()
            left += 1
        ans += right - left + 1
    print(ans)
                
    

if __name__ == '__main__':
    solve()
    #run_tests(solve)








    