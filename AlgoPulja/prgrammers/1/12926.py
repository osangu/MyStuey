def solution(s: str, n):
    ind_vs_val = {ind + 1: val for ind, val in enumerate('abcdefghijklmnopqrstuvwxyz')}
    val_vs_ind = {val: ind + 1 for ind, val in enumerate('abcdefghijklmnopqrstuvwxyz')}

    answer = ''

    for val in s:

        if val == ' ':
            answer += ' '
            continue

        elif val.isupper():
            val = val.lower()
            ind = val_vs_ind[val] + n if val_vs_ind[val] + n <= 26 else val_vs_ind[val] + n - 26
            answer += ind_vs_val[ind].upper()

        else:
            ind = val_vs_ind[val] + n if val_vs_ind[val] + n <= 26 else val_vs_ind[val] + n - 26
            answer += ind_vs_val[ind]

    return answer