array = list(map(int, input().split()))
h = array[:3]
w = array[3:]

check_array = None


def reset():
    global check_array
    check_array = [[0 for i in range(3)] for j in range(3)]


def check(check_array):
    for i in range(3):
        if check_array[i][0] + check_array[i][1] + check_array[i][2] != h[i]:
            return False
        if check_array[0][i] + check_array[1][i] + check_array[2][i] != w[i]:
            return False
        for j in range(3):
            if check_array[i][j] <= 0:
                return False
    return True


def main():
    global check_array
    result = 0
    for v00 in range(min(h[0], w[0]), 0, -1):
        reset()
        check_array[0][0] = v00
        for v01 in range(min(h[0] - v00, w[1]), 0, -1):
            v02 = h[0] - v00 - v01
            if v02 <= 0:
                continue
            check_array[0][1] = v01
            check_array[0][2] = v02
            for v10 in range(min(h[1], w[0] - v00), 0, -1):
                check_array[1][0] = v10
                for v11 in range(min(h[1] - v10, w[1] - v01), 0, -1):
                    v12 = h[1] - v10 - v11
                    if v12 <= 0 or check_array[0][2] + v12 > w[2]:
                        continue
                    check_array[1][1] = v11
                    check_array[1][2] = v12

                    check_array[2][0] = w[0] - v00 - v10
                    check_array[2][1] = w[1] - v01 - v11
                    check_array[2][2] = w[2] - v02 - v12

                    if check(check_array):
                        result += 1
    print(result)


main()