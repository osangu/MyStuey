# https://gethlemn.tistory.com/17
def solution(strings, n):
    return sorted(sorted(strings), key=lambda str: str[n])

# 아래는 3개만 통과한 내 코드...
'''
def solution(strings, n):
    abc = {}

    for i, j in enumerate(strings): abc[j[n:]] = i

    index_list = list(abc.keys())
    index_list.sort()

    answer = []

    for j in index_list:
        answer.append(
            strings[abc[j]]
        )
    return answer
'''




