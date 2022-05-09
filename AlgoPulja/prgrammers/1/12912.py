def solution(a, b):
    if a > b:
        return sum([i for i in range(b, a + 1)])
    else:
        return sum([i for i in range(a, b + 1)])


# 다른 사람 풀이
'''
    def solution(a, b)
    
        if b > a: a, b = b, a
        
        return sum(range(a,b + 1))
    
'''