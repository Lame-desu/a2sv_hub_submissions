# Problem: Skibidus and Fanum Tax (hard version) - http://codeforces.com/problemset/problem/2065/C2

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

def findMinGreater(num, m_ints):
    i, j = 0, len(m_ints) - 1
    
    while i <= j:
        mid = (i + j) // 2
        if m_ints[mid]  >= num: 
            j = mid - 1  
        else:
            i = mid + 1 

    return -1 if i >= len(m_ints) else m_ints[i]  # Ensure failure case is correctly handled


def solve():
    n, m = read_ints()
    n_ints = read_ints()
    m_ints = read_ints()
    m_ints = sorted(m_ints)
    n_ints[0] = min(n_ints[0], m_ints[0]-n_ints[0])

    for i in range(1, len(n_ints)):
        min_greater = findMinGreater(n_ints[i-1] + n_ints[i], m_ints)

        if min_greater == -1:
            if n_ints[i] >= n_ints[i-1]:
                continue
            else:
                print("NO")
                return
        elif min_greater - n_ints[i] >= n_ints[i-1] and n_ints[i] >= n_ints[i-1]:
            n_ints[i] = min(min_greater - n_ints[i], n_ints[i])

        elif min_greater - n_ints[i] >= n_ints[i-1]:
            n_ints[i] = min_greater - n_ints[i]
        else:
            print("NO")
            return
    print("YES")

if __name__ == '__main__':
    # solve()
    run_tests(solve)