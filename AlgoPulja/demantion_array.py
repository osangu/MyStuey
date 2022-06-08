def solution(x, y):
    answer = [[(j + 1) + (10 * i) for j in range(y)] for i in range(x)]
    print(answer)


if __name__ == '__main__': solution(5, 10)
