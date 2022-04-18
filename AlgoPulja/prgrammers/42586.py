import math


def solution(progresses, speeds):
    day = []
    for i in range(0, len(progresses)):
        progresses[i] = 100 - progresses[i]

        if progresses[i] % speeds[i] == 0:
            day.append(math.trunc(progresses[i] / speeds[i]))
        else:
            day.append(math.trunc((progresses[i] / speeds[i])) + 1)

    answer = []
    count = 0
    num = day[0]

    for i in range(1, len(day)):
        count += 1
        if num >= day[i]:
            continue
        else:
            num = day[i]
            answer.append(count)
            count = 0
    answer.append(count + 1)
    return answer


if __name__ == '__main__':
    solution([93, 30, 55], [1, 30, 5])
    solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
    solution([20, 99, 93, 30, 55, 10], [5, 10, 1, 1, 30, 5])
    solution([1, 99], [99, 1])
