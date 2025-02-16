# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    array = list(map(int, input().split()))

    i = sum = total_sum = 0
    while i < n:
        while i < n and array[i] < 0:
            sum = array[i] if sum == 0 else max(sum, array[i])
            i += 1
        total_sum += sum
        sum = 0
        while i < n and array[i] > 0:
            sum = max(sum, array[i])
            i += 1
        total_sum += sum
        sum = 0
    print(total_sum)
