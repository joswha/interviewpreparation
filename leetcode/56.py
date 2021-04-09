def merge(intervals):
    res = []
    intervals.sort(key = lambda x: x[0])
    for interval in intervals:
        if not res or res[-1][1] < interval[1]:
            res.append(interval)
        else:
            res[-1][1] = max(res[-1][1], interval[1])
    return



intervals = [[1,4], [0,4]]
print(merge(intervals))