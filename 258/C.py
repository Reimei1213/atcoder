N, Q = map(int, input().split())
S = list(input())
query = [list(map(int, input().split())) for _ in range(Q)]

current_x = 0
for q, x in query:
    if q == 1:
        current_x = (current_x + x) % N
    else:
        print(S[(x - current_x - 1) % N])
