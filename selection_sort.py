def selection_sort(input):

    for i in range(len(input)):
        min = i

        for j in range(i+1, len(input)):
            if input[min] > input[j]:
                min = j

        input[i], input[min] = input[min], input[i]
    return input
