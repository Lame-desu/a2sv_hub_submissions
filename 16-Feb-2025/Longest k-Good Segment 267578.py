# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

n, k = list(map(int, input().split()))
array = list(map(int, input().split()))

answer = [0, -1]
left = 0
character_length = {}
for right in range(n):
    character_length[array[right]] = character_length.get(array[right], 0) + 1
    while len(character_length) > k:
        character_length[array[left]] -= 1
        if character_length[array[left]] == 0:
            del character_length[array[left]]
        left += 1
    if right - left > answer[1] - answer[0]:
        answer = [left +1 , right + 1]
print(*answer)