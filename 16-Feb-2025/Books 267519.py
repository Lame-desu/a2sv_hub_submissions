# Problem: Books - https://codeforces.com/contest/279/problem/B

n, t = list(map(int, input().split()))
array = list(map(int, input().split()))

left = sum = count = 0
for right in range(n):
    sum += array[right]
    while sum > t:
        sum -= array[left]
        left += 1
    count = max(count, right - left + 1)
print(count)