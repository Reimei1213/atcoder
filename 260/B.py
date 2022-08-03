N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split())) # 数学
B = list(map(int, input().split())) # 英語

passed = []
for _ in range(X):
	idx = A.index(max(A))
	passed.append(idx)
	A[idx] = -1
	B[idx] = -1

for _ in range(Y):
	idx = B.index(max(B))
	passed.append(idx)
	A[idx] = -1
	B[idx] = -1

sum_list = [A[i]+B[i] for i in range(N)]
for _ in range(Z):
	idx = sum_list.index(max(sum_list))
	passed.append(idx)
	sum_list[idx] = -2

for r in sorted(passed):
	print(r+1)