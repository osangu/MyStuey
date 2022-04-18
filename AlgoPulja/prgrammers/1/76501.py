def solution(absolutes, signs):
    answer = 0
    for i in range(0, len(absolutes)):

        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]

    return answer

if __name__ == '__main__':
    solution([4, 7, 12],[True, False, True])