def moveElementToEnd(array, toMove):
    
    i = 0
    j = len(array) - 1

    while i < j:
        if array[i] == toMove:
            # print(f"i: {i}, value: {array[i]}")
            while array[j] == toMove:
                j -= 1         # arry[j] surely won't be `toMove` after this point
                if i >= j:
                    break
                # print(f"j: {j}, value: {array[j]}")
            aux = array[j]
            array[j] = array[i]
            array[i] = aux
            # print(array)
        i += 1

    return array