def solution(id_list, report, k):
    id_vs_reported = {}
    reporter_vs_reported = {}
    will_banned = []
    answer = []

    for i in id_list:
        id_vs_reported[i] = []
        reporter_vs_reported[i] = []
        answer.append(0)

    for i in report:
        j = i.split()

        if not j[0] in id_vs_reported[j[1]]: id_vs_reported[j[1]].append(j[0])

        if not j[1] in reporter_vs_reported[j[0]]: reporter_vs_reported[j[0]].append(j[1])

    for i in id_vs_reported:

        if len(id_vs_reported[i]) >= k: will_banned.append(i)

    for ind, val in enumerate(reporter_vs_reported):

        for j in reporter_vs_reported[val]:

            if j in will_banned: answer[ind] += 1

    return answer