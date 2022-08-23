from collections import defaultdict
import heapq

Q = int(input())
queries = [list(map(int, input().split())) for _ in range(Q)]
S = defaultdict(int)
mx = []
mn = []

for q in queries:
    if q[0] == 1:
        x = q[1]
        S[x] += 1
        heapq.heappush(mx, -x)
        heapq.heappush(mn, x)
    
    if q[0] == 2:
        x, c = q[1:]
        S[x] = max(0, S[x] - c)

    if q[0] == 3:
        while S[-mx[0]] == 0:
            heapq.heappop(mx)
        while S[mn[0]] == 0:
            heapq.heappop(mn)
        print(-mx[0]-mn[0])