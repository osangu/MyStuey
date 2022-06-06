from sys import stdin
n, m, b = map(int, stdin.readline().split())
arr = [[list(map(int, stdin.readline().split()))] for i in range(n)]
for i in arr:
    print(i)