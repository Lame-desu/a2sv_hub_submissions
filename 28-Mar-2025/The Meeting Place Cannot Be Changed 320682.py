# Problem: The Meeting Place Cannot Be Changed - https://codeforces.com/problemset/problem/780/B

import sys
import itertools

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

def isValid(second, x, v):
    mn_right = float("inf")
    mx_left = float("-inf")

    for pos, speed in zip(x, v):
        delta = speed * second
        right  = pos + delta
        left = pos - delta
        mn_right = min(mn_right, right)
        mx_left = max(mx_left, left)
    return mx_left <= mn_right


def solve():
    n = read_int()
    x = read_ints()
    v = read_ints()
    
    min_time, max_time = 0, max(x) - min(x)
    percision = 10 ** (-6)
    while max_time - min_time > percision:
        mid = (max_time + min_time) / 2
        if isValid(mid, x, v):
            max_time = mid
        else:
            min_time = mid
    print(max_time)

if __name__ == '__main__':
    solve()
    #run_tests(solve)