def solution(s):
    a = [i for i in s]

    return (a.count('p') + a.count('P')) == (a.count('y') + a.count('Y'))

