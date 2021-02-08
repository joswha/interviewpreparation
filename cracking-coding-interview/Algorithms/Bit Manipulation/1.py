# You are given two 32 bit numbers, N and M and two bit positions i and j. Write a method to insert M into N from the certain position i to position j


def insertion(N, M, i, j):
    elements_N = [int(n) for n in str(N)]
    elements_M = [int(m) for m in str(M)]
    k = len(elements_M) - 1
    for index in range(len(elements_N) - i, j - i - 1, -1):
        elements_N[index] = elements_M[k] | elements_N[index]
        k -= 1
    
    print(elements_N)

# DRIVER CODE

N = 10000000000
M = 10011

insertion(N, M, 2, 6)