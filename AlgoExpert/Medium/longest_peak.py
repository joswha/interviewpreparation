def longestPeak(array):
    # window = []
    curr_len = max_len = 0
    inc = False
    dec = False
    for i in range(len(array) - 1):
        if array[i] < array[i + 1] and dec is False:
            curr_len += 1
            inc = True
            inc = False
        elif array[i] > array[i + 1] and inc is True:
            curr_len += 1
            dec = True
            inc = False


tc = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longestPeak(tc))