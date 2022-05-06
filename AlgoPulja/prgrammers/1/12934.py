def solution(n):
    mit = n ** (1 / 2) # 1/2을 제곱하면 루트가 적용되니까 바로 밑 구하는 방법..개천재다 이 사람..

    return (mit + 1) ** 2 if not mit % 1 else -1