def solution(n):
    mit = n ** (1 / 2)

    return (mit + 1) ** 2 if not mit % 1 else -1