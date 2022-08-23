N = int(input())

memo = [0] * N

for i in range(0, N):
    tmp = []
    for j in range(0, i+1):
        if j == 0 or i == j:
            tmp.append(1)
        else:
            tmp.append(memo[j-1] + memo[j])
    memo = tmp
    print(' '.join(map(str, memo)))
