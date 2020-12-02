def insertion_sort(input):
    for i in range(len(input) - 1):
        if input[i] > input[i+1]:
            small = i+1

            for j in range(small, 0, -1):
                if input[j] < input[j-1]:
                    input[j], input[j-1] = input[j-1], input[j]

    return input