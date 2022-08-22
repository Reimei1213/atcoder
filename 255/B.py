from cmath import inf
import math

N, K = map(int, input().split())
A = list(map(int, input().split()))
coordinate = []
for _ in range(N):
    coordinate.append(list(map(int, input().split())))

result = 0
for i, c in enumerate(coordinate):
    x, y = c
    tmp = math.inf
    for a in A:
        base_x, base_y = coordinate[a-1]
        tmp = min(tmp, (x - base_x)**2 + (y - base_y)**2)
    result = max(result, tmp)
print(math.sqrt(result))
