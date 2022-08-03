
S = list(input())
T = list(input())

flag = True
if len(S) > len(T):
    flag = False
else:
    i = 0
    j = 0
    while j < len(T):
        if i < len(S) and S[i] == T[j]:
            i += 1
            j += 1
        else:
            if T[j] == S[i-1] and S[i-1] == S[i-2]:
                j += 1
            else:
                flag = False
                break

if flag:
    print("Yes")
else:
    print("No")