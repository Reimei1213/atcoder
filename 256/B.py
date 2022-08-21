N = int(input())
A = list(map(int, input().split()))

p = 0
masu = [False]*4

for a in A:
    masu[0] = True
    for i, m in enumerate(reversed(masu)):
        i = 3 - i
        if not m: continue
        if i + a > 3:
            p += 1
            masu[i] = False
            continue
        masu[i] = False
        masu[i + a] = True
print(p)