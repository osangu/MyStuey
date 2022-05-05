def solution_by_for(x, n):
    answer = [x * i for i in range(1, n + 1)]
    return answer


def solution_by_lambda(x, n): return list(map(lambda i: x * (i + 1), range(n)))
