def solution(dartResult: str):
    a = ''
    for i in dartResult:
        try:
            int(i)
            a += i
        except:
            a += i + ' '
    a = a.split()
    for i, j in enumerate(a):
        if len(j) != 1:
            if j[-1] == 'S': a[i] = int(j[:-1])
            elif j[-1] == 'D': a[i] = int(j[:-1]) ** 2
            elif j[-1] == 'T': a[i] = int(j[:-1]) ** 3

    for i, j in enumerate(a):
        if j == '#':
            a[i - 1] *= -1
            a.pop(i)

    for i, j in enumerate(a):
        if j == '*':
            if i == 1: a[0] *= 2
            elif i == 2:
                a[0] *= 2
                a[1] *= 2
            elif i == 3:
                a[2] *= 2
                if type(a[1]) == int: a[1] *= 2
                else: a[0] *= 2
            elif i == 4:
                a[1] *= 2
                a[3] *= 2
            elif i == 5:
                a[2] *= 2
                a[4] *= 2
    for i in range(3):
        if '*' in a: a.remove('*')
    return sum(a)
