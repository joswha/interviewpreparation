def numberOfMatches(n):
    matches = 0
    while(n > 1):
        matches += n // 2
        n = (n + 1) // 2
    return matches

print(numberOfMatches(4))