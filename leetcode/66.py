def plusOne(digits):
    number = 0
    res = []
    for digit in digits:
        number += digit
        number *= 10

    number //= 10
    number += 1

    while number:
        res.insert(0, number % 10)
        number //= 10
    return res

digits = [1,2,3]
plusOne(digits)
