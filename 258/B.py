N = int(input())
A = [list(input()) for _ in range(N)]
z = ""
for i in range(N):
    for j in range(N):
        s1 = ""
        s2 = ""
        s3 = ""
        s4 = ""
        s5 = ""
        s6 = ""
        s7 = ""
        s8 = ""
        for k in range(N):
            s1 += A[i][(j+k) % N]
            s2 += A[i][(j-k) % N]
            s3 += A[(i+k) % N][j]
            s4 += A[(i-k) % N][j]
            s5 += A[(i+k) % N][(j+k) % N]
            s6 += A[(i-k) % N][(j+k) % N]
            s7 += A[(i+k) % N][(j-k) % N]
            s8 += A[(i-k) % N][(j-k) % N]
        z = max(s1, s2, s3, s4, s5, s6, s7, s8, z)
print(z)