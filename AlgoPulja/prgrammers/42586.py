import math


def solution(progresses, speeds):
    day = []
    answer = []
    for i in range(0, len(progresses)):
        progresses[i] = 100 - progresses[i]

        if progresses[i] % speeds[i] == 0:
            day.append(math.trunc(progresses[i] / speeds[i]))
        else:
            day.append(math.trunc((progresses[i] / speeds[i])) + 1)

    a = day[0]
    count = 1
    # [7, 3, 9]
    # [5, 10, 1, 1, 20, 1]

    for i in range(1, len(day)):
        if a >= day[i]:
            a = day[i]
            count += 1
            continue
        else:
            a = day[i]
            answer.append(count)
            count = 1

    answer.append(count)

    return answer