# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

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
    n, k = read_ints()
    array = read_ints()
    gaps = [0]
    for i in range(1, n):
        gaps.append(array[i]-array[i-1])
    emited_gaps = sum(sorted(gaps, reverse=True)[:k-1])
    print(array[-1] - array[0] - emited_gaps)
if __name__ == '__main__':
    solve()
    #run_tests(solve)