def slices(series, length):
    result = []
    if length > len(series) or length <= 0:
        raise ValueError("length is out of bounds")

    for index in range(len(series) - length + 1):
        # print(series[index:index + length])
        result.append(series[index:index + length])

    return result

# print(slices('12345', 3))