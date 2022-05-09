def solution(d, budget):
    answer = 0

    if sum(d) <= budget:
        answer = len(d)

    else:
        d.sort()
        print(d)
        for ind, val in enumerate(d):

            if val > budget:
                answer = ind
                break
            else:
                budget -= val

    return answer