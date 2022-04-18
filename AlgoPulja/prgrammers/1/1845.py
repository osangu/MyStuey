def solution(nums):
    selection = []

    for i in nums:

        try:
            selection.index(i)
        except ValueError:
            selection.append(i)

    if len(selection) > len(nums) / 2:
        return len(nums) / 2

    else:
        return len(selection)
