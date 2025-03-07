# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

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
    array = read_ints()
    count = i = 0
    while i < len(array) - 1:
        if array[i] > array[i+1]:
            count += 1
            i+=1
        i+=1
    print(count)

if __name__ == '__main__':
    # solve()
    run_tests(solve)