def solution(seoul):

    for i in enumerate(seoul):
        if i[1] == 'Kim': return f"김서방은 {i[0]}에 있다"