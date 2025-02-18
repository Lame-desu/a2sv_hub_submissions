# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n, k, q = map(int, input().split())
interval = []
for _ in range(n):
    interval.append(list(map(int, input().split())))

queries = []
for _ in range(q):
    queries.append(list(map(int, input().split())))

count_array = [0] * 200002
for start, end in interval:
    count_array[start] += 1
    count_array[end + 1] -= 1

for i in range(1, len(count_array)):
    count_array[i] += count_array[i - 1]

for i in range(len(count_array)):
    if count_array[i] >= k:
        count_array[i] = 1
    else:
        count_array[i] = 0

for i in range(1, len(count_array)):
    count_array[i] += count_array[i - 1]

for query in queries:
    start, end = query
    count = count_array[end] - count_array[start - 1]
    print(count)