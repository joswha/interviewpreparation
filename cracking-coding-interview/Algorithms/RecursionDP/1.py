# Triple Step: A child is running the staircase, n steps; can hop either 1, 2, or 3 steps. How many possbile ways can the child run? /≥

# def tripleStep(n):
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
#     return tripleStep(n - 3) + tripleStep(n - 2) + tripleStep(n - 1)
# print(tripleStep(4))

def countWays(n):
    memo = [-1] * (n + 1)
    return tripleStep(n, memo)

def tripleStep(n, memo):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif memo[n] > -1:
        return memo[n]
    else:
        memo[n] = tripleStep(n - 1, memo) + tripleStep(n - 2, memo) + tripleStep(n - 3, memo)
        return memo[n]

print(countWays(4))
