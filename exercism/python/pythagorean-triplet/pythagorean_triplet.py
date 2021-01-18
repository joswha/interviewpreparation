def triplets_with_sum(number):
    return [[a,b,c] for a in range(1, number + 1) for b in range(a, number + 1) for c in range(b, number + 1) if a ** 2 + b ** 2 == c ** 2 and a + b + c == number]