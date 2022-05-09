def solution(arr, divisor):
    arr = [i for i in arr if not i % divisor]

    arr.sort()

    if len(arr) == 0: return [-1]

    return arr
