def solution(s: str):
    lower = [i for i in s if i.islower()]
    upper = [i for i in s if i.isupper()]

    lower.sort(reverse=True)
    upper.sort(reverse=True)

    answer = ''
    for i in lower: answer += i
    for j in upper: answer += j

    return answer