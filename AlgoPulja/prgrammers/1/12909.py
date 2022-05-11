def solution(s):
    answer = []
    for i in s:

        if answer:
            if (answer[-1] == '(') and i == ')':
                answer.pop()
                continue
        answer.append(i)

    return not answer

# 내가 원했던 코드
'''
def is_pair(s):
    open_cnt = 0
    for c in s:
        if c == '(': open_cnt += 1
        elif c == ')': open_cnt -= 1
            if open_cnt < 0: return False
    return open_cnt == 0
'''