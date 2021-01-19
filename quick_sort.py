def quick_sort(input):

    left_sort = []
    right_sort = []


    if len(input) <= 1:
        return input

    pivot = input.pop()
    for num in input:
        if num > pivot:
            right_sort.append(num)
        else:
            left_sort.append(num)

    return quick_sort(left_sort) + [pivot] + quick_sort(right_sort)