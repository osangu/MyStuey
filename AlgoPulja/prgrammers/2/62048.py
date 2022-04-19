def solution(w, h):
    all_piece = w * h
    ch_gong = 0

    if w != h:
        for i in range(1, w + 1):
            if w % i == 0 and h % i == 0: ch_gong = i
        return all_piece - (w + h) + ch_gong

    else:
        return all_piece - w
