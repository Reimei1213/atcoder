N = int(input())
S = input()
W = list(map(int, input().split()))

people = []
count = 0
for n in range(N):
    people.append((W[n], S[n]))
    if S[n] == '1':
        count += 1

people.sort()
result = count
for n in range(N):
    w, s = people[n]
    if s == '1': count -= 1
    if s == '0': count += 1
    if n+1 == N or people[n+1][0] != w:
        result = max(result, count)

print(result)