t = int(input())
for j in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]
    current = input()
    goodness = 0
    for i in range(0, n // 2):
        if current[i] != current[n - i - 1]:
            goodness += 1
    print("Case #" + str(j) + ": " + str(abs(k - goodness)))  
