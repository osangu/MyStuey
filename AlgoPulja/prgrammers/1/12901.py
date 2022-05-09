def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

    for i in range(0, a - 1): b += month[i]

    return days[(b - 3) % 7]