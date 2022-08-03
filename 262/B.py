N, M = map(int, input().split())
path_data = [list(map(int, input().split())) for _ in range(M)]
path = [[0] * N for _ in range(N)]

for u, v in path_data:
	u -= 1
	v -= 1
	path[u][v] = 1
	path[v][u] = 1

result = 0
for u in range(N-2):
	for v in range(u+1, N-1):
		for w in range(v+1, N):
			if path[u][v] == 1 and path[v][w] == 1 and path[w][u] == 1:
				result += 1

print(result)