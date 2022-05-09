def solution(board, moves):
    basket = []
    answer = 0
    for i in moves:
        for j in board:
            if j[i - 1] == 0:
                continue
            else:
                if len(basket) > 0 and basket[-1] == j[i - 1]:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(j[i - 1])
                j[i - 1] = 0
                break
    return answer
