H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
start = None
goal = None
for i in range(H):
    for j in range(W):
        if S[i][j] == 'o':
            if start:
                goal = (i, j)
            else:
                start = (i, j)
print(abs(start[0] - goal[0]) + abs(start[1] - goal[1]))