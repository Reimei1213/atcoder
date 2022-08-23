from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))
d = defaultdict(list)
for i, a in enumerate(A):
    d[i%K].append(a)

for a in d:
    d[a].sort(reverse=True)

cnt = 0
result_array = []
while True:
    for i in range(K):
        if d[i]:
            result_array.append(d[i].pop())
            cnt += 1
    if cnt == N:
        break

for i in range(1, N):
    if result_array[i] < result_array[i-1]:
        print('No')
        exit()
print('Yes')