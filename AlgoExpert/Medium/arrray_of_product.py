def arrayOfProducts(array):
    # left = right = res = [1 for i in range(len(array))]
    left = [1 for i in range(len(array))]
    right = [1 for i in range(len(array))]
    res = [1 for i in range(len(array))]

    # print(left, right)
    product = 1

    for i in range(len(array)):
        left[i] = product
        product *= array[i]
    
    product = 1 
    
    for i in reversed(range(len(array))):
        right[i] = product
        product *= array[i]

    for i in range(len(array)):
        res[i] = left[i] * right[i]

    return res