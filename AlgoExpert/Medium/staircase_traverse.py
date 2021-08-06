def staircaseTraversal(height, maxSteps):
    current_ways = 0
    total_ways = [1]

    for current_height in range(1, height + 1):
        start = current_height - maxSteps - 1
        end = current_height - 1

        if start >= 0:
            current_ways -= total_ways[start]

        current_ways += total_ways[end]
        total_ways.append(current_ways)

    return total_ways[height]