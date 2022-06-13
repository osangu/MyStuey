count = 0


def solution():
    num = int(input())

    print(fib(num), fib2(num))


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib2(n):
    f = [1] * (n + 1)
    cnt = 0
    for i in range(3, n + 1):
        cnt += 1
        f[i] = f[i - 1] + f[i - 2]

    return cnt  # f[n]이 원래 값임
