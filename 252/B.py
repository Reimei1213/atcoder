N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mx = max(A)
result = "No"
for i, a in enumerate(A):
    if mx == a and i+1 in B:
        result = "Yes"
        break

print(result)
