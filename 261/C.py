N = int(input())
A = [input() for _ in range(N)]

memo = {}
for a in A:
	if a in memo:
		print(a + "(" + str(memo[a]) + ")")
		memo[a] += 1
	else:
		memo[a] = 1
		print(a)