def mergeOverlappingIntervals(intervals):
    sort_intervals = sorted(intervals, key = lambda x: x[0]) # sort them based on initial value

    merged = []
    current = [sort_intervals[0]]

    merged.append(current)

    for next in sort_intervals:
        curr_end = current[1]
        next_start = next[0]
        next_end = next[1]

        if curr_end >= next_start:
            current[1] = max(curr_end, next_end)
        else:
            current = next
            merged.append(current)
    return merged

tab = [
  [1, 2],
  [3, 5],
  [4, 7],
  [6, 8],
  [9, 10]
]

print(mergeOverlappingIntervals(tab))