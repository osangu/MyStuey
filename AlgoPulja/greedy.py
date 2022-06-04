def solution(money: int):
    answer = 0
    for i in [500, 100, 50, 10]:

        if money > i:
            answer += money // i
            money %= i

    print(answer)


if __name__ == '__main__': solution(1270)
