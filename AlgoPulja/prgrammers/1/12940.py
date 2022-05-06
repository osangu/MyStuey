def solution(n, m):
    answer = []

    for i in range(1, n + 1):
        if n % i == 0 and m % i == 0:
            answer.append(i)

    if len(answer) != 1: answer = [answer[-1]]

    for i in range(1, m * n + 1):
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break

    return answer