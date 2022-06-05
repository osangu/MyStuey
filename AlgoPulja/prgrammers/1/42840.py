def solution(answers):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    p1_len = len(p1)
    p2_len = len(p2)
    p3_len = len(p3)
    record = [0,0,0]
    answer = []
    for i in range(len(answers)):
        if p1[i % p1_len] == answers[i]: record[0] += 1
        if p2[i % p2_len] == answers[i]: record[1] += 1
        if p3[i % p3_len] == answers[i]: record[2] += 1
    max_record = max(record)
    for i in range(len(record)):
        if record[i] == max_record: answer.append(i + 1)
    return answer