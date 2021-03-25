def maxProfit(prices):
    i = 0
    valley = peak = profit = 0
    n = len(prices) - 1
    while i < n:
        while i < n and prices[i] >= prices[i + 1]:
            i += 1
        valley = prices[i]
        while i < n and prices[i] <= prices[i + 1]:
            i += 1
        peak = prices[i]
        profit += (peak - valley)
    return profit

a = [7,1,5,3,6,4]
b = [1,2,3,4,5]
# print(b)
print(maxProfit(b))