def shell_sort(input):

    size = len(input)
    interval = size//2

    while interval > 0:
            for i in range(interval, size):
                t = input[i]
                j = i
                while j >= interval and input[j - interval] > t:
                    input[j] = input[j - interval]
                    j -= interval
    
                input[j] = t
            interval = interval // 2

    return input