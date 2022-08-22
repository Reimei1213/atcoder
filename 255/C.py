X, A, D, N = map(int, input().split())


def tree(x, left, right):
    global A, D
    mid = (right + left) // 2
    tmp = A + D * mid
    if tmp + D > x and tmp - D < x:
        return mid

    if left == right: return mid

    if D > 0:
        if tmp > x:
            return tree(x, left, mid)
        elif tmp < x:
            return tree(x, mid + 1, right)
        else:
            return mid
    else:
        if tmp < x:
            return tree(x, left, mid)
        elif tmp > x:
            return tree(x, mid + 1, right)
        else:
            return mid


n = tree(X, 0, N-1)
result = abs((A + D * n) - X)
if n > 0:
    result = min(result, abs((A + D * (n-1)) - X))
elif n < N - 1:
    result = min(result, abs((A + D * (n+1)) - X))
print(result)