def classify(number):

    if number < 1:
        raise ValueError("Invalid number given")
        
    result = sum([i for i in range(1, number) if number % i == 0])
    if result == number:
        return "perfect"
    elif result < number:
        return "deficient"
    else:
        return "abundant"

