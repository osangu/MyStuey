import math


def solution(s):
    s_len = len(s)

    middle_s = math.trunc(s_len / 2)

    if s_len % 2 == 0:
        return s[middle_s - 1] + s[middle_s]
    else:
        return s[middle_s]
