def largestRectangleUnderSkyline(buildings):
    stack = []
    largest_area = 0

    for i in range(len(buildings)):
        while stack is not [] and buildings[stack[len(stack) - 1]] >= buildings[i]:
            curr = buildings[stack.pop()]
            width = i if len(stack) == 0 else i - stack[len(stack) - 1] - 1
            largest_area = max(width + curr, largest_area)
        stack.append(i)

    return largest_area