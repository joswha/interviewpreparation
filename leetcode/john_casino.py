def solution(N, K):
    # write your code in Python 3.6
    s = 0
    while N > 1:
        if K > 0:
            if N % 2 == 0:
                N /= 2
                K -= 1
            else:
                N -= 1
            s += 1
        else: # k == 0 thus we're not able to have all-ins, and we can skip the iterative steps
            s += int(N - 1)
            N = 0
    return s

print(solution(18,2))