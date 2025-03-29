# Problem: Limited Repainting - https://codeforces.com/contest/2070/problem/C

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

def validate_p(strip, penalities, k, p):
    
    flip = 0
    opp = 0
    for char, pen in zip(strip, penalities):
        if char == "B" and pen > p and not flip:
            opp += 1
            flip = 1
        elif char == "R" and pen > p and flip:
            flip = 0

        if opp > k:
            return False
    return True

def solve():
    n, k = read_ints()
    strip = input()
    penalities = read_ints()

    min_p, max_p = 0, max(penalities)
    while min_p <= max_p:
        mid = (min_p + max_p) // 2

        if validate_p(strip, penalities, k, mid):
            max_p = mid - 1
        else:
            min_p = mid + 1

    print(min_p)


if __name__ == '__main__':
    # solve()
    run_tests(solve)