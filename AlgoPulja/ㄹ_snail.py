def solution(x, y):
    answer = []
    cnt = 1
    for i in range(x):
        answer.append([])

        for j in range(y)[::cnt]:
            answer[i].append((j + 1) + 10 * i)

        cnt = -1
    print(answer)


if __name__ == '__main__': solution(5, 10)
