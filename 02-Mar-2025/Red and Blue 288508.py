# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

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

def solve():
    n = read_int()
    array1 = read_ints()
    m = read_int()
    array2 = read_ints()

    for i in range(1, n):
        array1[i] += array1[i-1]
    for j in range(1, m):
        array2[j] += array2[j-1]
    
    print(max(0, max([0] + array1) + max([0] + array2)))

if __name__ == '__main__':
    # solve()
    run_tests(solve)