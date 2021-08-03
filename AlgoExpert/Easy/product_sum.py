# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, multiplier = 1):
    total_sum = 0
    for elem in array:
        if type(elem) is not list:
            total_sum += elem
        else:
            total_sum += productSum(elem, multiplier + 1)
    return total_sum * multiplier # this applies PER EACH RECURSIVE CALL(since the whole function is re-executed all over again)


arr = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(productSum(arr))