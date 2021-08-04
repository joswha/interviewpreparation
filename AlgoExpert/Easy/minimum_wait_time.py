def minimumWaitingTime(queries):
    queries.sort()

    total = 0
    for i, q in enumerate(queries):
        q_left = len(queries) - (i + 1)
        total += q * q_left
    
    return total