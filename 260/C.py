N, X, Y = map(int, input().split())
blue_list = [0] * 11
red_list = [0] * 11
red_list[N] = 1

def red(l, n):
	red_list[l-1] += 1 * n
	blue_list[l] += X * n

def blue(l, n):
	red_list[l-1] += 1 * n
	blue_list[l-1] += Y * n

for level in range(N, 1, -1):
	red(level, red_list[level])
	blue(level, blue_list[level])
print(blue_list[1])