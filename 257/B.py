N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for l in L:
    if A[l-1] == N or l != K and A[l-1]+1 == A[l]: continue
    A[l-1] += 1
print(' '.join(map(str, A)))
