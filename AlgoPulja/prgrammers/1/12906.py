def solution(arr):
    new_one = []

    for i in arr:

        if len(new_one) > 0 and new_one[-1] == i: new_one.pop()

        new_one.append(i)

    return new_one
