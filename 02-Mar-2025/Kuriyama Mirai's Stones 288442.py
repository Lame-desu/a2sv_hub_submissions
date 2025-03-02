# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

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
    n_arry = read_ints()
    m = read_int()
    m_queries = read_matrix(m)
    sorted_arry = sorted(n_arry)

    first_prefix, second_prefix = [0] * (n + 1), [0] * (n + 1)
    sum1 = sum2 = 0
    for i in range(n):
        sum1 += n_arry[i]
        sum2 += sorted_arry[i]
        first_prefix[i+1] = sum1
        second_prefix[i+1] = sum2
    # print(first_prefix, second_prefix)
    for type, l, r in m_queries:
        print(first_prefix[r] - first_prefix[l-1] if type == 1 else second_prefix[r] - second_prefix[l-1])
if __name__ == '__main__':
    solve()
    #run_tests(solve)