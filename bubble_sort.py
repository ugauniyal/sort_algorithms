def bubble_sort(input):

    size = len(input)

    for i in range(len(input) - 1,0,-1):
            for j in range(i):
                if input[j] > input[j+1]:
                    input[j], input[j+1] = input[j+1], input[j]
                else:
                    j = j+1

    return input