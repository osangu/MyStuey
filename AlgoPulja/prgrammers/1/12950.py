def solution(arr1, arr2):
    for i in range(0, len(arr1)):
        for j in range(0, len(arr2[i])):
            arr1[i][j] += arr2[i][j]

    return arr1


if __name__ == '__main__': solution(

    [[1, 2, 3], [2, 3, 4]],

    [[3, 4, 3], [5, 6, 5]]
)
