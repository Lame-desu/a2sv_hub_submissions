# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

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
    query = []
    for i in range(n-1):
        query.append(read_int())
    check_valid = [[0, 0] for i in range(n)]

    for i in range(n-1, -1, -1):
        if sum(check_valid[i]) == 0:
            check_valid[query[i-1]-1][0] += 1
        elif check_valid[i][0] >= 3:
            check_valid[query[i-1] -1][1] += 1
        else:
            print("No")
            return
    if check_valid[0][0] >= 3:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()
    #run_tests(solve)