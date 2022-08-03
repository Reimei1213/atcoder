N = int(input())
A = [list(c for c in input()) for _ in range(N)]

result = "correct"
for i in range(N):
	for j in range(i+1, N):
		if not (A[i][j] == "D" and A[j][i] == "D" or A[i][j] == "W" and A[j][i] == "L" or A[i][j] == "L" and A[j][i] == "W"):
			result = "incorrect"

print(result)